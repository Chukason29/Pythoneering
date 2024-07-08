class Country:
    def __init__(this, name, continent, president):
        this.name = name
        this.continent = continent
        this.president = president
    
    def changePresident(self, presName): # The self parameter is just a python conventii
        self.presName = presName
        return self.presName

#changing object properties
myCountry = Country("Nigeria", "Africa", "Tinubu")
print(myCountry.name) #prints Nigeria

myCountry.name = "South Africa"
print(myCountry.name) #prints South Africa


#get 20% off all the products in the database
class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category