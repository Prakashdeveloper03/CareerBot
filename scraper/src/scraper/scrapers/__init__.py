from ..jobs import Enum, BaseModel, JobType, JobResponse, Country, DescriptionFormat


class Site(Enum):
    """
    Enumeration representing different job search sites.
    """

    LINKEDIN = "linkedin"
    INDEED = "indeed"
    GLASSDOOR = "glassdoor"


class ScraperInput(BaseModel):
    """
    Input parameters for job scraping.

    Attributes:
        site_type (list[Site]): List of job search sites to scrape.
        search_term (str | None): The search term for job listings. Defaults to None.
        location (str | None): The location to search for jobs. Defaults to None.
        country (Country | None): The country for job search. Defaults to Country.USA.
        distance (int | None): The distance from the location to consider. Defaults to None.
        is_remote (bool): Whether to consider remote jobs. Defaults to False.
        job_type (JobType | None): The type of job to search for. Defaults to None.
        easy_apply (bool | None): Whether to consider easy apply jobs. Defaults to None.
        offset (int): The offset for job listings. Defaults to 0.
        linkedin_fetch_description (bool): Whether to fetch LinkedIn job descriptions. Defaults to False.
        linkedin_company_ids (list[int] | None): LinkedIn company IDs to filter jobs. Defaults to None.
        description_format (DescriptionFormat | None): The format for job descriptions. Defaults to DescriptionFormat.MARKDOWN.
        results_wanted (int): The number of job listings desired. Defaults to 15.
        hours_old (int | None): The age of job listings to consider. Defaults to None.
    """

    site_type: list[Site]
    search_term: str | None = None
    location: str | None = None
    country: Country | None = Country.USA
    distance: int | None = None
    is_remote: bool = False
    job_type: JobType | None = None
    easy_apply: bool | None = None
    offset: int = 0
    linkedin_fetch_description: bool = False
    linkedin_company_ids: list[int] | None = None
    description_format: DescriptionFormat | None = DescriptionFormat.MARKDOWN
    results_wanted: int = 15
    hours_old: int | None = None


class Scraper:
    """
    Base class for job scraping.

    Attributes:
        site (Site): The job search site to scrape.
        proxy (dict | None): Proxy settings for scraping. Defaults to None.
    """

    def __init__(self, site: Site, proxy: list[str] | None = None):
        """
        Initialize the Scraper instance.

        Parameters:
            site (Site): The job search site to scrape.
            proxy (list[str] | None): Proxy settings for scraping. Defaults to None.
        """
        self.site = site
        self.proxy = (lambda p: {"http": p, "https": p} if p else None)(proxy)

    def scrape(self, scraper_input: ScraperInput) -> JobResponse:
        """
        Method to perform scraping.

        Parameters:
            scraper_input (ScraperInput): Input parameters for scraping.

        Returns:
            JobResponse: Response containing scraped job listings.
        """
        ...
