import re

def extract_emails(text):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

    emails = re.findall(email_pattern, text)
    return emails

text = """
Hello, This is urooj baloch you can contact me through email balochurooj2005@gmail.com or k230071@nu.edu.pk
"""

extracted_emails = extract_emails(text)
print("Extracted Email Addresses: ")
for email in extracted_emails:
    print(email)