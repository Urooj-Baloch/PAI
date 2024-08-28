url = input("Enter a URL starting with 'http://www.': ")
if url.startswith('http://www.'):
    new_url = url[11:] + '.com'
    print("Formatted URL:", new_url)
else:
    print("The URL does not start with 'http://www.'")
