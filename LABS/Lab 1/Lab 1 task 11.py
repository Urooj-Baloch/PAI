marks = {}
marks['S1'] = int(input("Enter marks for Subject 1: "))
marks['S2'] = int(input("Enter marks for Subject 2: "))
marks['S3'] = int(input("Enter marks for Subject 3: "))
totalSubjects = 3
total_marks = 0
subWithHighestMarks = None
highest_marks = -1
for subject in marks:
    mark = marks[subject]
    total_marks += mark
average_marks = total_marks / totalSubjects
percentage_marks = (total_marks / 300) * 100
print("Average marks:",average_marks)
print("Percentage:",percentage_marks,"%")


