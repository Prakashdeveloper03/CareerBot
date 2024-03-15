import re
import logging
import numpy as np

import html2text
import tls_client
import requests
from requests.adapters import HTTPAdapter, Retry

from ..jobs import JobType

# HTML to Markdown converter instance
text_maker = html2text.HTML2Text()

# Logger configuration
logger = logging.getLogger("Scraper")
logger.propagate = False
if not logger.handlers:
    logger.setLevel(logging.ERROR)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.ERROR)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)


def count_urgent_words(description: str) -> int:
    """
    Count the number of urgent words in a job description.

    Parameters:
        description (str): The job description text.

    Returns:
        int: The count of urgent words found in the description.
    """
    urgent_patterns = re.compile(
        r"\burgen(t|cy)|\bimmediate(ly)?\b|start asap|\bhiring (now|immediate(ly)?)\b",
        re.IGNORECASE,
    )
    matches = re.findall(urgent_patterns, description)
    count = len(matches)

    return count


def markdown_converter(description_html: str):
    """
    Convert HTML description to Markdown format.

    Parameters:
        description_html (str): The HTML formatted job description.

    Returns:
        str: The converted Markdown formatted description.
    """
    if description_html is None:
        return ""
    text_maker.ignore_links = False
    try:
        markdown = text_maker.handle(description_html)
        return markdown.strip()
    except AssertionError as e:
        return ""


def extract_emails_from_text(text: str) -> list[str] | None:
    """
    Extract email addresses from a text.

    Parameters:
        text (str): The text containing email addresses.

    Returns:
        list[str] | None: List of email addresses found in the text, or None if no emails found.
    """
    if not text:
        return None
    email_regex = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
    return email_regex.findall(text)


def create_session(
    proxy: dict | None = None,
    is_tls: bool = True,
    has_retry: bool = False,
    delay: int = 1,
) -> requests.Session:
    """
    Create and configure a requests session.

    Parameters:
        proxy (dict | None): Proxy settings for the session. Defaults to None.
        is_tls (bool): Whether to use TLS for the session. Defaults to True.
        has_retry (bool): Whether to include retry logic for the session. Defaults to False.
        delay (int): Delay factor for retry logic. Defaults to 1.

    Returns:
        requests.Session: Configured requests session.
    """
    if is_tls:
        session = tls_client.Session(random_tls_extension_order=True)
        session.proxies = proxy
    else:
        session = requests.Session()
        session.allow_redirects = True
        if proxy:
            session.proxies.update(proxy)
        if has_retry:
            retries = Retry(
                total=3,
                connect=3,
                status=3,
                status_forcelist=[500, 502, 503, 504, 429],
                backoff_factor=delay,
            )
            adapter = HTTPAdapter(max_retries=retries)

            session.mount("http://", adapter)
            session.mount("https://", adapter)
    return session


def get_enum_from_job_type(job_type_str: str) -> JobType | None:
    """
    Get JobType enum from its string representation.

    Parameters:
        job_type_str (str): String representation of the JobType.

    Returns:
        JobType | None: JobType enum if found, else None.
    """
    res = None
    for job_type in JobType:
        if job_type_str in job_type.value:
            res = job_type
    return res


def currency_parser(cur_str):
    """
    Parse currency string into numeric value.

    Parameters:
        cur_str (str): The currency string to parse.

    Returns:
        float: The parsed numeric value of the currency.
    """
    cur_str = re.sub("[^-0-9.,]", "", cur_str)
    cur_str = re.sub("[.,]", "", cur_str[:-3]) + cur_str[-3:]
    if "." in list(cur_str[-3:]):
        num = float(cur_str)
    elif "," in list(cur_str[-3:]):
        num = float(cur_str.replace(",", "."))
    else:
        num = float(cur_str)
    return np.round(num, 2)
