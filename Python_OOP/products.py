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

for x, y in productData.items():
    myProduct = Product()
    newPrice = myProduct.slashPrice(y["price"], 50)
    productData[x]["price"] = newPrice
    
