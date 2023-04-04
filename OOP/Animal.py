class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        match self.species:
            case "Dog":
                return "Woof Woof"
            case "Cat":
                return "Meow Meow"
            case _:
                return "..^..^.."
            
animal = Animal("Dakota", "Dog")

print(animal.speak())