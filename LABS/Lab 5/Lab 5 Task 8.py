import re
def extract_dates(text):
    date_pattern = r'\b\d{2}/\d{2}/\d{4}\b'
    dates = re.findall(date_pattern, text)
    return dates
text = """
Here are some important dates:
- The project started on 12/09/2023.
- The deadline is 2023-09-12.
- Remember to attend the meeting on 10/12/2023.
- Invalid dates like 30/02/2023 and 2023-13-01 should not be included.
"""
extracted_dates = extract_dates(text)
print("Extracted Dates (DD/MM/YYYY):")
for date in extracted_dates:
    print(date)
