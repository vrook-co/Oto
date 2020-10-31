from lepl.apps.rfc3696 import HttpUrl


def validate_url(self, url):
	"""Validate a HTTP URL.

	Args:
		url (str): a URL in string form

	Returns:
		bool: True if valld, False otherwise
	"""
	validator = HttpUrl()

	return validator(url)


