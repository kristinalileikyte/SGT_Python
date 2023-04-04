from Person import Person

class Teacher(Person):
    def __init__(self, name, age, address, subject):
        super().__init__(name, age, address)
        self.subject = subject

    def workdays(self):
        match self.subject:
            case "History":
                return "Mondays and Wednesdays"
            case "Math":
                return "Tuesdays and Fridays"
            case "Spanish":
                return "Thursdays"
            case _:
                return "--Error--"
            
teacher = Teacher("Jack", 30, "Pepper St. 22", "Math")

print(f"Your classes will be on {teacher.workdays()}.")