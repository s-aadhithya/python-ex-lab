import re
import validate_email
import dns.resolver

def validate_email_address(email):

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return "Invalid email format. Please provide a valid email address."

    is_valid = validate_email.validate_email(email)

    if is_valid:
        domain = email.split('@')[1]
        try:
            dns.resolver.resolve(domain, 'MX')
            return f"{email} is a valid email address with valid DNS records."
        except dns.resolver.NoAnswer:
            return f"Valid email address, but no DNS records found for {domain}."
        except dns.resolver.NXDOMAIN:
            return f"No DNS domain found for {domain}."
    else:
        return "Invalid email address. Please provide a valid email address."

email_address = input("Enter an email address to validate: ")
validation_result = validate_email_address(email_address)
print(validation_result)