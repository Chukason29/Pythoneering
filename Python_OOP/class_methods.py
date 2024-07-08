class Car:
    def __init__(self, name, model, colour) :
        self.name = name
        self.model = model
        self.colour = colour
    
    def ChangeColor(this):
        this.colour = "Red"
        return this.colour


myCar = Car("Benz", "A54", "White")
print(myCar.ChangeColor()) #Prints Red instead of white, because ChangeColor was specific