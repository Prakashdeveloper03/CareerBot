from typing import Optional, List
from datetime import date
from enum import Enum
from pydantic import BaseModel


class JobType(Enum):
    """Enumeration for different types of job positions."""

    FULL_TIME = (
        "fulltime",
        "100%",
    )
    PART_TIME = ("parttime",)
    CONTRACT = ("contract", "contractor")
    TEMPORARY = ("temporary",)
    INTERNSHIP = ("internship",)
    PER_DIEM = ("perdiem",)
    NIGHTS = ("nights",)
    OTHER = ("other",)
    SUMMER = ("summer",)
    VOLUNTEER = ("volunteer",)


class Country(Enum):
    """Enumeration for different countries."""

    AUSTRALIA = ("australia", "au", "com.au")
    CANADA = ("canada", "ca", "ca")
    INDIA = ("india", "in", "co.in")
    UK = ("uk,united kingdom", "uk", "co.uk")
    USA = ("usa,us,united states", "www", "com")
    US_CANADA = ("usa/ca", "www")
    WORLDWIDE = ("worldwide", "www")

    @property
    def indeed_domain_value(self) -> str:
        """Returns the domain value for Indeed."""
        return self.value[1]

    @property
    def glassdoor_domain_value(self) -> str:
        """Returns the domain value for Glassdoor."""
        if len(self.value) == 3:
            subdomain, _, domain = self.value[2].partition(":")
            if subdomain and domain:
                return f"{subdomain}.glassdoor.{domain}"
            else:
                return f"www.glassdoor.{self.value[2]}"
        else:
            raise Exception(f"Glassdoor is not available for {self.name}")

    def get_url(self) -> str:
        """Returns the URL for the country."""
        return f"https://{self.glassdoor_domain_value}/"

    @classmethod
    def from_string(cls, country_str: str) -> "Country":
        """Converts a string to a Country enum value."""
        country_str = country_str.strip().lower()
        for country in cls:
            country_names = country.value[0].split(",")
            if country_str in country_names:
                return country
        valid_countries = [country.value for country in cls]
        raise ValueError(
            f"Invalid country string: '{country_str}'. Valid countries are: {', '.join([country[0] for country in valid_countries])}"
        )


class Location(BaseModel):
    """Model representing job location."""

    country: Optional[Country] = None
    city: Optional[str] = None
    state: Optional[str] = None

    def display_location(self) -> str:
        """Returns the formatted location."""
        location_parts = []
        if self.city:
            location_parts.append(self.city)
        if self.state:
            location_parts.append(self.state)
        if self.country and self.country not in (Country.US_CANADA, Country.WORLDWIDE):
            country_name = self.country.value[0]
            if "," in country_name:
                country_name = country_name.split(",")[0]
            if country_name in ("usa", "uk"):
                location_parts.append(country_name.upper())
            else:
                location_parts.append(country_name.title())
        return ", ".join(location_parts)


class CompensationInterval(Enum):
    """Enumeration for different compensation intervals."""

    YEARLY = "yearly"
    MONTHLY = "monthly"
    WEEKLY = "weekly"
    DAILY = "daily"
    HOURLY = "hourly"

    @classmethod
    def get_interval(cls, pay_period: str) -> str:
        """Returns the compensation interval based on the pay period."""
        interval_mapping = {
            "YEAR": cls.YEARLY,
            "HOUR": cls.HOURLY,
        }
        if pay_period in interval_mapping:
            return interval_mapping[pay_period].value
        else:
            return cls[pay_period].value if pay_period in cls.__members__ else None


class Compensation(BaseModel):
    """Model representing compensation details."""

    interval: Optional[CompensationInterval] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
    currency: Optional[str] = "USD"


class DescriptionFormat(Enum):
    """Enumeration for different description formats."""

    MARKDOWN = "markdown"
    HTML = "html"


class JobPost(BaseModel):
    """Model representing a job post."""

    title: str
    company_name: str
    job_url: str
    location: Optional[Location]

    description: Optional[str] = None
    company_url: Optional[str] = None

    job_type: Optional[List[JobType]] = None
    compensation: Optional[Compensation] = None
    date_posted: Optional[date] = None
    benefits: Optional[str] = None
    emails: Optional[List[str]] = None
    num_urgent_words: Optional[int] = None
    is_remote: Optional[bool] = None


class JobResponse(BaseModel):
    """Model representing a response containing job posts."""

    jobs: List[JobPost] = []
