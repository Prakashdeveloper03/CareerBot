class LinkedInException(Exception):
    """
    Exception raised for errors related to LinkedIn scraping.

    Attributes:
        message (str): Explanation of the error.
    """

    def __init__(self, message=None):
        """
        Initialize the LinkedInException.

        Parameters:
            message (str): Explanation of the error. Defaults to None.
        """
        super().__init__(message or "An error occurred with LinkedIn")


class IndeedException(Exception):
    """
    Exception raised for errors related to Indeed scraping.

    Attributes:
        message (str): Explanation of the error.
    """

    def __init__(self, message=None):
        """
        Initialize the IndeedException.

        Parameters:
            message (str): Explanation of the error. Defaults to None.
        """
        super().__init__(message or "An error occurred with Indeed")


class GlassdoorException(Exception):
    """
    Exception raised for errors related to Glassdoor scraping.

    Attributes:
        message (str): Explanation of the error.
    """

    def __init__(self, message=None):
        """
        Initialize the GlassdoorException.

        Parameters:
            message (str): Explanation of the error. Defaults to None.
        """
        super().__init__(message or "An error occurred with Glassdoor")
