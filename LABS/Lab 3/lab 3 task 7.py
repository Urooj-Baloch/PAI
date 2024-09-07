try:
    # Read the content from the file
    with open('/Users/urooj/Desktop/replacement_needed.txt', 'r') as file:
        original_text = file.read()

    print("Original text:", original_text)

    # Prompt the user to enter the incorrect and correct letters
    incorrect_letter = input('Enter the incorrect letter: ')
    correct_letter = input('Enter the correct letter: ')

    # Validate the inputs to ensure they are single characters
    if len(incorrect_letter) != 1 or len(correct_letter) != 1:
        print("Error: Both incorrect and correct letters should be a single character.")
    else:
        # Replace the incorrect letter with the correct one
        corrected_text = original_text.replace(incorrect_letter, correct_letter)

        print("Corrected text:", corrected_text)

        # Write the corrected text to a new file
        with open('corrected_replacement_needed.txt', 'w') as corrected_file:
            corrected_file.write(corrected_text)

except FileNotFoundError:
    print("Error: The file 'replacement_needed.txt' was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
