file = 'C:/Users/student24/Desktop/Task 2.txt'
search_text = 'urooj'
replace_text = 'Ayesha'
try:
    with open(file, 'r') as file:
        content = file.read()
        print("Original content:")
        print(content)
    modified = content.replace(search_text, replace_text)
    print("\nModified content:")
    print(modified)
    with open(file, 'w') as file:
        file.write(modified)
    print("\nReplacement successful.")
except FileNotFoundError:
    print(f"Error: The file '{file}' was not found.")
except IOError:
    print(f"Error: An I/O error occurred while accessing the file '{file}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
