
grades = []
sum = 0
with open("grades.csv") as file:
    for line in file:
        name, grade = line.rstrip().split(",")
        grades.append(int(grade))
        sum += int(grade)

average = f"{sum / len(grades)}"
with open("average.csv","w") as file:
    file.write(average)