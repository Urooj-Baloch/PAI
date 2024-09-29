class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def display_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Student Name: {self.name}")


class Marks(Student):
    def __init__(self, student_id, name):
        super().__init__(student_id, name)
        self.marks_dict = {}

    def add_marks(self, subject, marks):
        self.marks_dict[subject] = marks

    def display_marks(self):
        print("Marks Obtained:")
        for subject, mark in self.marks_dict.items():
            print(f"{subject}: {mark}")


class Result(Marks):
    def __init__(self, student_id, name):
        super().__init__(student_id, name)

    def calculate_total_and_average(self):
        total = sum(self.marks_dict.values())
        average = total / len(self.marks_dict) if self.marks_dict else 0
        return total, average

    def display_result(self):
        total, average = self.calculate_total_and_average()
        self.display_info()
        self.display_marks()
        print(f"Total Marks: {total}")
        print(f"Average Marks: {average:.2f}")
if __name__ == "__main__":
    student_result = Result("S789", "Urooj Baloch")
    student_result.add_marks("Algorithm", 85)
    student_result.add_marks("Data Science", 90)
    student_result.add_marks("Calculus", 80)
    student_result.display_result()
