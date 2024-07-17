class Car:
    def __init__(self, name, model, colour) :
        self.name = name
        self.model = model
        self.colour = colour
    
    def ChangeColor(self, colour):
        self.colour = colour
        return self.colour


myCar = Car("Benz", "A54", "White")
print(myCar.ChangeColor("Blue")) #Prints blue instead of white, because ChangeColor was specific
print(myCar.colour)