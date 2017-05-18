# DEFINE REGEX
import re
def password_detection():
	password = raw_input('Enter a password to test: ')

	length_regex = re.compile(r'.{8,}')
	uppercase_regex = re.compile(r'[A-Z]')
	lowercase_regex = re.compile(r'[a-z]')
	digit_regex = re.compile(r'[0-9]')

	return(length_regex.search(password) is not None
		and uppercase_regex.search(password) is not None
		and lowercase_regex.search(password) is not None
		and digit_regex.search(password) is not None)

print(password_detection())