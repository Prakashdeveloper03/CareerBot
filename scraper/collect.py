import csv
from scraper import scrape

# List of top job roles to scrape
top_jobs = [
    "AI Specialist",
    "AR Developer",
    "Account Executive",
    "Aerospace Engineer",
    "Application Support Analyst",
    "Artificial Intelligence Engineer",
    "Automation Engineer",
    "Back-end Developer",
    "Big Data Engineer",
    "Biomedical Engineer",
    "Blockchain Developer",
    "Brand Manager",
    "Business Analyst",
    "Business Development Manager",
    "Business Intelligence Developer",
    "CRM Developer",
    "Chemical Engineer",
    "Civil Engineer",
    "Clinical Psychologist",
    "Cloud Engineer",
    "Cloud Solutions Architect",
    "Cloud Solutions Developer",
    "Computer Forensics Investigator",
    "Computer Hardware Engineer",
    "Computer Network Architect",
    "Computer Programmer",
    "Computer Systems Analyst",
    "Computer and Information Research Scientist",
    "Computer and Information Systems Manager",
    "Content Manager",
    "Counseling Psychologist",
    "Credit Analyst",
    "Cybersecurity Analyst",
    "Data Analyst",
    "Data Center Support Specialist",
    "Data Engineer",
    "Data Scientist",
    "Data Warehouse Architect",
    "Database Administrator",
    "Database Developer",
    "DevOps Engineer",
    "Digital Marketing Manager",
    "Digital Marketing Specialist",
    "ERP Consultant",
    "Electrical Engineer",
    "Embedded Systems Engineer",
    "Embedded Systems Software Developer",
    "Enterprise Architect",
    "Environmental Engineer",
    "Financial Analyst",
    "Financial Planner",
    "Front-end Developer",
    "Full Stack Developer",
    "GIS Specialist",
    "Game Developer",
    "Health IT Specialist",
    "IT Auditor",
    "IT Consultant",
    "IT Director",
    "IT Manager",
    "IT Project Manager",
    "IT Risk Analyst",
    "IT Sales Professional",
    "IT Security Consultant",
    "IT Support Specialist",
    "IT Technician",
    "IT Trainer",
    "Industrial Engineer",
    "Information Security Analyst",
    "Information Security Manager",
    "Integration Specialist",
    "Investment Banker",
    "IoT Developer",
    "Linux System Administrator",
    "Machine Learning Engineer",
    "Market Research Analyst",
    "Marketing Manager",
    "Mechanical Engineer",
    "Mobile App Developer",
    "Mobile Application Architect",
    "Multimedia Artist/Animator",
    "Network Administrator",
    "Network Architect",
    "Network Engineer",
    "Network Security Engineer",
    "Penetration Tester",
    "Petroleum Engineer",
    "Quality Assurance Engineer",
    "Risk Manager",
    "SEO Specialist",
    "Sales Engineer",
    "Sales Manager",
    "Sales Representative",
    "Social Media Manager",
    "Social Media Manager",
    "Software Architect",
    "Software Developer",
    "Software Development Manager",
    "Software Engineer",
    "Software Quality Assurance (QA) Tester",
    "Solution Architect",
    "System Security Administrator",
    "Systems Administrator",
    "Systems Analyst",
    "Systems Analyst",
    "Systems Engineer",
    "Technical Support Specialist",
    "Technical Writer",
    "UI Designer",
    "UI/UX Designer",
    "UX Designer",
    "UX Researcher",
    "VR Developer",
    "Web Developer",
    "Wireless Network Engineer",
]

# Loop through each job role
for job_role in top_jobs:
    # Scrape job listings for the current job role from multiple sites
    jobs = scrape(
        sites=["indeed", "linkedin", "glassdoor"],  # Specify the sites to scrape
        search_term=job_role,  # Search term (job role)
        job_count=100,  # Number of job listings to scrape
    )

    # Print the number of jobs found for the current job role
    print(f"Found {len(jobs)} jobs for {job_role}")

    # Print the first few job listings for the current job role
    print(jobs.head())

    # Save the scraped job listings to a CSV file
    jobs.to_csv(
        f"./data/{job_role}_jobs.csv",  # File path for saving the CSV file
        quoting=csv.QUOTE_NONNUMERIC,  # Quoting mode for CSV writer
        escapechar="\\",  # Character used to escape special characters
        index=False,  # Do not include row indices in the CSV file
    )

    # Print a success message after completing the scraping and saving process
    print(f"Successfully completed scraping and saving for {job_role}")
