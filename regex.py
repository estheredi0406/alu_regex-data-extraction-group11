import re

# 1. Email Validation
def validate_email(email):
    pattern = r'[A-Za-z0-9-_.]+@[A-Za-z0-9.]+\.[A-Za-z]{2,}'
    return bool(re.match(pattern, email))

# 2. URL Validation
def validate_url(url):
    pattern = r'https?:\/\/[A-Za-z0-9.-]+(?:\.[A-Za-z]{2,})(?:\/[^\s]*)?'
    return bool(re.match(pattern, url))


# 3. Phone Number Validation
def validate_phone_number(phone):
    patterns = [
        r'\(?\d{3}\)?[ .-]?\d{3}[.-]?\d{4}',
        r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}']
    return any(bool(re.match(p, phone)) for p in patterns)

# 4. Credit Card Validation
def validate_credit_card(card):
    patterns = [
        r'\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}',
        r'^\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}$']
        
    return any(bool(re.match(p, card)) for p in patterns)
