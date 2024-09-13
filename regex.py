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

# 7. Hashtag Validation
def validate_hashtag(hashtag):
    patterns = [
        r'#[A-Za-z0-9_]+',
        r'#\w+'
    ]
    return any(bool(re.match(p, hashtag)) for p in patterns)

# 8. Currency Validation
def validate_currency(currency):
    pattern = r'\$\d{1,3}(,\d{3})*(\.\d{2})?'
    return bool(re.match(pattern, currency))

# Function to prompt user for input and validate based on choice
def run_validation():
    print("Choose a type of data to validate:")
    print("1. Email")
    print("2. URL")
    print("3. Phone Number")
    print("4. Credit Card")
    print("5. Time")
    print("6. HTML Tag")
    print("7. Hashtag")
    print("8. Currency")
    
    choice = input("Enter your choice (1-8): ")
    
    if choice == '1':
        email = input("Enter an email to validate: ")
        print("Valid Email" if validate_email(email) else "Invalid Email")
    
    elif choice == '2':
        url = input("Enter a URL to validate: ")
        print("Valid URL" if validate_url(url) else "Invalid URL")
    
    elif choice == '3':
        phone = input("Enter a phone number to validate: ")
        print("Valid Phone Number" if validate_phone_number(phone) else "Invalid Phone Number")
    
    elif choice == '4':
        card = input("Enter a credit card number to validate: ")
        print("Valid Credit Card" if validate_credit_card(card) else "Invalid Credit Card")
    
    elif choice == '5':
        time = input("Enter a time to validate: ")
        print("Valid Time" if validate_time(time) else "Invalid Time")
    
    elif choice == '6':
        tag = input("Enter an HTML tag to validate: ")
        print("Valid HTML Tag" if validate_html_tag(tag) else "Invalid HTML Tag")
    
    elif choice == '7':
        hashtag = input("Enter a hashtag to validate: ")
        print("Valid Hashtag" if validate_hashtag(hashtag) else "Invalid Hashtag")
    
    elif choice == '8':
        currency = input("Enter a currency amount to validate: ")
        print("Valid Currency" if validate_currency(currency) else "Invalid Currency")
    
    else:
        print("Invalid choice. Please select a number between 1 and 8.")

# Main loop to keep the program running until the user decides to quit
if __name__ == "_main_":
    while True:
        run_validation()
        another = input("Do you want to validate another? (yes/no): ").strip().lower()
        if another != 'yes':
            break

print("Thank you for using the validator! 🧑‍💻")
