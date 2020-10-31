"""

This is a helper function that is meant to be used to download videos for cloud sources such as OneDrive, DropBox, Google-Drive, etc.

"""
import re

def download(url, *args, **kwargs):

    """

    #TODO

    - Fill this with the documentation of the code. i.e. the docstring.
    - Find a way to validate the url, return error if the URL is not in format.

    - Add arguments to accomadate for different cloud providers.

    - Add requirements to requirements.txt usign "pip freeze > requirements"

    - Make downloads resumable if it has any network issues.

    """
    regex = re.compile(
        r'^https?://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'
        r'localhost|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    if not regex.search(url):
        raise Exception("Error! Given URL is not a valid URL.")

#Calling download func for testing
download("https://google.com")
