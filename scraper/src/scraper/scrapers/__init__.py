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
    Base class for implementing job scraper for different job search sites.
    """

    def __init__(self, site: Site, proxy: list[str] | None = None):
        """
        Initialize the scraper with the specified site and proxy settings.

        Args:
            site (Site): The job search site.
            proxy (list[str] | None): List of proxy URLs. Defaults to None.
        """
        self.site = site
        self.proxy = (lambda p: {"http": p, "https": p} if p else None)(proxy)

    def scrape(self, scraper_input: ScraperInput) -> JobResponse:
        """
        Scrapes job listings based on the provided input.

        Args:
            scraper_input (ScraperInput): Input parameters for job scraping.

        Returns:
            JobResponse: Response containing the scraped job listings.
        """
        ...
