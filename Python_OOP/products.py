"""
A product page
"""
productData = {
    "item1":{
        "name":"Phone",
        "price": 3000,
        "category": "Electronics",
        "colour": "Red"
    },
    "item2":{
        "name":"Shoe",
        "price": 500,
        "category": "fashion",
        "colour": "White"
    },
    "item3":{
        "name":"Toy Car",
        "price": 1000,
        "category": "Kiddies",
        "colour": "Blue"
    }
}
class Product:   
    def slashPrice(self, price, priceSlash):
        return price * (1.00 - priceSlash/100)

for x, y in productData.items(): # for each item in productData
    myProduct = Product() #create a new object
    newPrice = myProduct.slashPrice(y["price"], 50) #apply slash price method
    productData[x]["price"] = newPrice #make the slashed price the new price
    print(f" {x}==>\n\t{y['price']} ") #print out the result
    
