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

# 5. Time Validation
def validate_time(time):
    patterns = [
        r'\d{1,}[:]\d{2}[ ]?([a-zA-Z]+)?',
        r'([0-9]+):[0-5][0-9] ?([APMapm]{2})?',
        r'\b([01]?[0-9]|2[0-3]):[0-5][0-9]([ a-zA-Z]+)?'
    ]
    return any(bool(re.match(p, time)) for p in patterns)

# 6. HTML Tag Validation
def validate_html_tag(tag):
    patterns = [
        r'<[^>]+>',
        r'<\s*[a-zA-Z]+(?:\s+[^>]+)?>',
        r'^\<[a-zA-Z0-9 =."]+\>$'
    ]
    return any(bool(re.match(p, tag)) for p in patterns)
