try:
    sentence = input("Enter a sentence: ")
    if sentence.strip().endswith('?'):
        with open('C:/Users/student24/Desktop/questions.txt', 'a') as file:
            file.write(sentence + '\n')
        print("The sentence has been written to 'questions.txt'.")
    else:
        print("The sentence is not a question and was not saved.")
except IOError:
    print("Error: An I/O error occurred while accessing the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
