marks = {}
marks['Physics'] = int(input("Enter marks for Physics: "))
marks['Chemistry'] = int(input("Enter marks for Chemistry: "))
marks['Maths'] = int(input("Enter marks for Maths: "))
totalSubjects = 3
total_marks = 0
subWithHighestMarks = None
highest_marks = -1
for subject in marks:
    mark = marks[subject]
    total_marks += mark
    if mark > highest_marks:
        highest_marks = mark
        subWithHighestMarks = subject
average_marks = total_marks / totalSubjects
print("Average marks:",average_marks)
print("Subject with the highest marks:",subWithHighestMarks ,"with" ,highest_marks, "marks")
