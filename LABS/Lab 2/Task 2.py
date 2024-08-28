def last_letter():
    word = input("Enter a word: ")
    last_letter = word.strip()[-1].lower()
    if last_letter.isalpha():##check whether the word is in alphabet letters or not
        if last_letter =='a' or last_letter =='e' or last_letter =='i' or last_letter =='o' or last_letter =='u':
            print("Last letter is Vowel")
        else:
            print("Last letter is Consonant")
    else:
        return "The last character is not a letter"


last_letter()
