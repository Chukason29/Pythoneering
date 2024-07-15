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
    def __init__(self, name, price, category, colour):
        self.name = name
        self.price = price
        self.category = category
        self.colour = colour
    