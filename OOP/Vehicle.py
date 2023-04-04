class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self) -> str:
        return f"Make: {self.make}\nModel: {self.model}\nYear: {self.year}"
    
    
class Car(Vehicle):
    def __init__(self, make, model, year, color):
        super().__init__(make, model, year)
        self.color = color

    def how_old(self):
        return 2023 - self.year
    

class Truck(Vehicle):
    def __init__(self, make, model, year, type):
        super().__init__(make, model, year)
        self.type = type

    def cargo(self):
        match self.type:
            case "refrigirator":
                return "Fish"
            case "tanker":
                return "Oil"
            case "cement-mixer":
                return "Cement"
            case "car-transporter":
                return "Vehicles"
            case _ :
                return "Empty"
            

car = Car("Mazda", 6, 2021, "black")
truck = Truck("GOURIKA", "2234", 2006, "tanker")

print(f"Your car is {car.how_old()} years old.")
print(f"Available cargo for yout truck: {truck.cargo()}.")
        