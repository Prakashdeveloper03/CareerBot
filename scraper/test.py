from scraper import scrape
import pandas as pd

# Scrape job listings for the specified search criteria
jobs: pd.DataFrame = scrape(
    site_name=["indeed", "linkedin"],  # Specify the sites to scrape
    search_term="software engineer",  # Search term (job title)
    location="Dallas, TX",  # Location filter for the job search
    results_wanted=10,  # Number of job listings wanted
    country_indeed="USA",  # Country filter for Indeed
)

# Save the scraped job listings to a CSV file
jobs.to_csv("../data/jobs.csv", index=False)

# Print the scraped job listings DataFrame
print(jobs.head())
