class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def get_info(self):
        return f"Name: {self.name} \nAge: {self.age} \nAddress: {self.address}"
    

person = Person("Bob", 25, "Los avenue, Los Angeles")

print(person.get_info())
        