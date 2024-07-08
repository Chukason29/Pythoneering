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


productData = {
    "item1":{
        "name":"Phone",
        "price": 3000,
        "category": "Electronics"
    },
    "item2":{
        "name":"Shoe",
        "price": 500,
        "category": "fashion"
    },
    "item3":{
        "name":"Toy Car",
        "price": 1000,
        "category": "Kiddies"
    }
}
#get 20% off all the products in the database using OOP
class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    def twentyPercentOff(self, price): #removes 20% from each item's price
        return price * 0.2
    
    def allproduct(self, db):
        for item in db:
            self.twentyPercentOff(item["price"])
    
