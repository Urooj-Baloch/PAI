l=[]
word=input("Enter any word: ")
print("Your entered word: ",word)
for i in word:
    l.append(i)
    reverse=word[::-1]

print("Word after reversed: ",reverse)
