import pandas as pd
from typing import Tuple
from concurrent.futures import ThreadPoolExecutor, as_completed

# Importing required classes and modules from local packages
from .jobs import JobType, Location
from .scrapers.indeed import IndeedScraper
from .scrapers.glassdoor import GlassdoorScraper
from .scrapers.linkedin import LinkedInScraper
from .scrapers import ScraperInput, Site, JobResponse, Country
from .scrapers.exceptions import (
    LinkedInException,
    IndeedException,
    GlassdoorException,
)


def scrape(
    sites: str | list[str] | Site | list[Site] | None = None,
    search_term: str | None = None,
    location: str | None = None,
    distance: int | None = None,
    is_remote: bool = False,
    job_type: str | None = None,
    easy_apply: bool | None = None,
    jobs_count: int = 15,
    country_indeed: str = "india",
    hyperlinks: bool = False,
    proxy: str | None = None,
    description_format: str = "markdown",
    linkedin_fetch_description: bool | None = False,
    linkedin_company_ids: list[int] | None = None,
    offset: int | None = 0,
    hours_old: int = None,
    **kwargs,
) -> pd.DataFrame:
    """
    Scrape job listings from various job sites.

    Parameters:
        sites (str | list[str] | Site | list[Site] | None): The sites to scrape. Defaults to None.
        search_term (str | None): The search term for job listings. Defaults to None.
        location (str | None): The location to search for jobs. Defaults to None.
        distance (int | None): The distance from the location to consider. Defaults to None.
        is_remote (bool): Whether to consider remote jobs. Defaults to False.
        job_type (str | None): The type of job to search for. Defaults to None.
        easy_apply (bool | None): Whether to consider easy apply jobs. Defaults to None.
        jobs_count (int): The number of jobs to scrape. Defaults to 15.
        country_indeed (str): The country for Indeed scraping. Defaults to "india".
        hyperlinks (bool): Whether to include hyperlinks in the output. Defaults to False.
        proxy (str | None): The proxy to use for scraping. Defaults to None.
        description_format (str): The format for job descriptions. Defaults to "markdown".
        linkedin_fetch_description (bool | None): Whether to fetch LinkedIn job descriptions. Defaults to False.
        linkedin_company_ids (list[int] | None): LinkedIn company IDs to filter jobs. Defaults to None.
        offset (int | None): The offset for job listings. Defaults to 0.
        hours_old (int): The age of job listings to consider. Defaults to None.
        **kwargs: Additional keyword arguments.

    Returns:
        pd.DataFrame: DataFrame containing scraped job listings.
    """

    # Mapping of site enum to scraper class
    SCRAPER_MAPPING = {
        Site.LINKEDIN: LinkedInScraper,
        Site.INDEED: IndeedScraper,
        Site.GLASSDOOR: GlassdoorScraper,
    }

    # Function to convert string to Site enum
    def map_str_to_site(sites: str) -> Site:
        return Site[sites.upper()]

    # Function to get JobType enum from value string
    def get_enum_from_value(value_str):
        for job_type in JobType:
            if value_str in job_type.value:
                return job_type
        raise Exception(f"Invalid job type: {value_str}")

    job_type = get_enum_from_value(job_type) if job_type else None

    # Function to get Site enum(s) based on input
    def get_site_type():
        site_types = list(Site)
        if isinstance(sites, str):
            site_types = [map_str_to_site(sites)]
        elif isinstance(sites, Site):
            site_types = [sites]
        elif isinstance(sites, list):
            site_types = [
                map_str_to_site(site) if isinstance(site, str) else site
                for site in sites
            ]
        return site_types

    country_enum = Country.from_string(country_indeed)

    # Prepare input for scraper
    scraper_input = ScraperInput(
        site_type=get_site_type(),
        country=country_enum,
        search_term=search_term,
        location=location,
        distance=distance,
        is_remote=is_remote,
        job_type=job_type,
        easy_apply=easy_apply,
        description_format=description_format,
        linkedin_fetch_description=linkedin_fetch_description,
        jobs_count=jobs_count,
        linkedin_company_ids=linkedin_company_ids,
        offset=offset,
        hours_old=hours_old,
    )

    # Function to scrape a site
    def scrape_site(site: Site) -> Tuple[str, JobResponse]:
        scraper_class = SCRAPER_MAPPING[site]
        scraper = scraper_class(proxy=proxy)
        scraped_data: JobResponse = scraper.scrape(scraper_input)
        return site.value, scraped_data

    site_to_jobs_dict = {}

    # Worker function for threading
    def worker(site):
        site_val, scraped_info = scrape_site(site)
        return site_val, scraped_info

    # Threading pool for scraping multiple sites concurrently
    with ThreadPoolExecutor() as executor:
        future_to_site = {
            executor.submit(worker, site): site for site in scraper_input.site_type
        }

        for future in as_completed(future_to_site):
            site_value, scraped_data = future.result()
            site_to_jobs_dict[site_value] = scraped_data

    jobs_dfs: list[pd.DataFrame] = []

    # Process scraped data
    for site, job_response in site_to_jobs_dict.items():
        for job in job_response.jobs:
            job_data = job.dict()
            job_data["job_url_hyper"] = (
                f'<a href="{job_data["job_url"]}">{job_data["job_url"]}</a>'
            )
            job_data["site"] = site
            job_data["company"] = job_data["company_name"]
            job_data["job_type"] = (
                ", ".join(job_type.value[0] for job_type in job_data["job_type"])
                if job_data["job_type"]
                else None
            )
            job_data["emails"] = (
                ", ".join(job_data["emails"]) if job_data["emails"] else None
            )
            if job_data["location"]:
                job_data["location"] = Location(
                    **job_data["location"]
                ).display_location()

            compensation_obj = job_data.get("compensation")
            if compensation_obj and isinstance(compensation_obj, dict):
                job_data["interval"] = (
                    compensation_obj.get("interval").value
                    if compensation_obj.get("interval")
                    else None
                )
                job_data["min_amount"] = compensation_obj.get("min_amount")
                job_data["max_amount"] = compensation_obj.get("max_amount")
                job_data["currency"] = compensation_obj.get("currency", "USD")
            else:
                job_data["interval"] = None
                job_data["min_amount"] = None
                job_data["max_amount"] = None
                job_data["currency"] = None

            job_df = pd.DataFrame([job_data])
            jobs_dfs.append(job_df)

    if jobs_dfs:
        jobs_df = pd.concat(jobs_dfs, ignore_index=True)
        desired_order: list[str] = [
            "job_url_hyper" if hyperlinks else "job_url",
            "site",
            "title",
            "company",
            "company_url",
            "location",
            "job_type",
            "date_posted",
            "interval",
            "min_amount",
            "max_amount",
            "currency",
            "is_remote",
            "num_urgent_words",
            "benefits",
            "emails",
            "description",
        ]
        return jobs_df[desired_order].sort_values(
            by=["site", "date_posted"], ascending=[True, False]
        )
    else:
        return pd.DataFrame()
