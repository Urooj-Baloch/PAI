file = 'C:/Users/student24/Desktop/mehak.txt'
try:
    with open(file, 'r') as file:
        content = file.read()
        numberOfCharacters = len(content)
        words = content.split()
        numberOfWords = len(words)
        print(f"Total number of characters: {numberOfCharacters}")
        print(f"Total number of words: {numberOfWords}")
except FileNotFoundError:
    print(f"Error: The file '{file}' was not found.")
except IOError:
    print(f"Error: An I/O error occurred while accessing the file '{file}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
