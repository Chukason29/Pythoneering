class Country:
    def __init__(this, name: str, continent: str, president: str): #Always type the your parameters to accept a particular datatypes
        this.name = name
        this.continent = continent
        this.president = president
    
    def changePresident(self, presName: str): # The self parameter is just a python conventii
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
    def twentyPercentOff(self, price: float): #removes 20% from each item's price
        return price - (price * 0.2)

    def allproduct(self, db: dict):
        for item in db:
            newPrice = self.twentyPercentOff(db[item]["price"]) #Calling a method from another method
            print(f"{db[item]["name"]}\n\t Old Price:{db[item]["price"]}\n\t New Price:{newPrice}")

myProduct = Product()
myProduct.allproduct(productData)


    
