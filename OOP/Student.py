from Person import Person

class Student(Person):
    def __init__(self, name, age, address, grade):
        super().__init__(name, age, address)
        self.grade = grade

    def birthyear(self):
        return 2023 - self.age
    
student = Student("Michael", 14, "Peter st. 17", 8)

print(student.birthyear())
print(student.get_info())
        