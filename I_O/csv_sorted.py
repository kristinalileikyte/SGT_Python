import csv


students = []

with open("grades.csv") as file:
    student_grades = csv.reader(file)
    for student in student_grades:
        students.append(student)

students.sort(key= lambda x: x[0])

with open("sorted_grades.csv","w") as file:
    writer = csv.writer(file)
    writer.writerows(students)