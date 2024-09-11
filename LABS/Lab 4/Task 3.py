class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def Print_biodata(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
S1 = Student("Urooj Baloch", 19)
S2 = Student("Mahnoor Hussain", 19)
print("___________________Here is the biodata of Student 1___________________")
S1.Print_biodata()
print("___________________Here is the biodata of Student 2___________________")
S2.Print_biodata()
