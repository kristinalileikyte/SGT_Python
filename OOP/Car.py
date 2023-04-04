class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self) -> str:
        return f"Make: {self.make}\nModel: {self.model}\nYear: {self.year}"
    

car = Car("Mazda",6,2021)
print(car.get_info())

