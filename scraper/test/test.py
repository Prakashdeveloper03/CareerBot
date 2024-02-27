from scraper import scrape_jobs
import pandas as pd

jobs: pd.DataFrame = scrape_jobs(
    site_name=["indeed", "linkedin", "zip_recruiter", "glassdoor"],
    search_term="software engineer",
    location="Dallas, TX",
    results_wanted=10,
    country_indeed="USA",
)

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
pd.set_option("display.width", None)
pd.set_option("display.max_colwidth", 50)
jobs.to_csv("../data/jobs.csv", index=False)
print(jobs)
