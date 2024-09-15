class Marks:
    def __init__(self, algo, dataScience, calculus):
        self.algo = algo
        self.dataScience = dataScience
        self.calculus = calculus
    def display_marks(self):
        print("Algorithm Marks:", self.algo)
        print("Data Science Marks:",self.dataScience)
        print("Calculus Marks:", self.calculus)
    def get_marks(self):
        return self.algo, self.dataScience, self.calculus
class Student:
    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks
    def display_info(self):
        print("Student ID:", self.student_id)
        print("Student Name:", self.name)
        self.marks.display_marks()
class Result:
    def __init__(self, student):
        self.student = student
    def calculate_results(self):
        algo, dataScience, calculus = self.student.marks.get_marks()
        total_marks = algo + dataScience + calculus
        average_marks = total_marks / 3
        return total_marks, average_marks
    def display_results(self):
        total, average = self.calculate_results()
        print("Total Marks:", total)
        print("Average Marks:", average)
marks = Marks(85, 90, 78)
student = Student("23k0071", "Urooj Baloch", marks)
result = Result(student)
student.display_info()
result.display_results()
