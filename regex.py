import re

# 1. Email Validation
def validate_email(email):
    pattern = r'[A-Za-z0-9-_.]+@[A-Za-z0-9.]+\.[A-Za-z]{2,}'
    return bool(re.match(pattern, email))

# 2. URL Validation
def validate_url(url):
    pattern = r'https?:\/\/[A-Za-z0-9.-]+(?:\.[A-Za-z]{2,})(?:\/[^\s]*)?'
    return bool(re.match(pattern, url))
