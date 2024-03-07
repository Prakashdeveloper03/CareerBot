class LinkedInException(Exception):
    """
    Exception raised for errors occurring during LinkedIn scraping.

    Attributes:
        message (str): Explanation of the error.
    """

    def __init__(self, message=None):
        """
        Initialize the LinkedInException.

        Args:
            message (str, optional): Explanation of the error. Defaults to None.
        """
        super().__init__(message or "An error occurred during LinkedIn scraping.")


class IndeedException(Exception):
    """
    Exception raised for errors occurring during Indeed scraping.

    Attributes:
        message (str): Explanation of the error.
    """

    def __init__(self, message=None):
        """
        Initialize the IndeedException.

        Args:
            message (str, optional): Explanation of the error. Defaults to None.
        """
        super().__init__(message or "An error occurred during Indeed scraping.")


class GlassdoorException(Exception):
    """
    Exception raised for errors occurring during Glassdoor scraping.

    Attributes:
        message (str): Explanation of the error.
    """

    def __init__(self, message=None):
        """
        Initialize the GlassdoorException.

        Args:
            message (str, optional): Explanation of the error. Defaults to None.
        """
        super().__init__(message or "An error occurred during Glassdoor scraping.")
