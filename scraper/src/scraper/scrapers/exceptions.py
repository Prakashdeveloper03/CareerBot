class LinkedInException(Exception):
    def __init__(self, message=None):
        super().__init__(message or "An error occurred with LinkedIn")


class IndeedException(Exception):
    def __init__(self, message=None):
        super().__init__(message or "An error occurred with Indeed")


class GlassdoorException(Exception):
    def __init__(self, message=None):
        super().__init__(message or "An error occurred with Glassdoor")
