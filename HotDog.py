"""Sub Class HotDog creates all of the hot dog objects"""
from Stock import Stock

class HotDog(Stock):

    def setToppings(self, type):
        if type == "Classic Dog":
            self.toppings = ["ketchup", "mustard"]
        elif type == "Atlanta Dog":
            self.toppings = ["chili", "slaw", "mustard"]
        elif type == "New York Dog":
            self.toppings = ["onions", "spicy mustard"]
        elif type == "Chicago Dog":
            self.toppings = ["mustard", "relish", "onion", "pickle", "pepper", "tomato"]
        elif type == "Chili Dog":
            self.toppings = ["chili", "onions", "cheese"]
        elif type == "Talon Dog":
            self.toppings = ["random"]
        else:
            self.toppings = ["None"]

    def getToppings(self):
        return self.toppings

    def setPrice(self, type):
        if type == "Classic Dog":
            self.price = 2.00
        elif type == "Atlanta Dog":
            self.price = 3.00
        elif type == "New York Dog":
            self.price = 3.00
        elif type == "Chicago Dog":
            self.price = 4.00
        elif type == "Chili Dog":
            self.price = 4.00
        elif type == "Talon Dog":
            self.price = 3.00
        else:
            self.price = 1.75

    def getPrice(self):
        return self.price

    def getDetails(self):
      print("Hot Dog: ", self.type)
      print("Toppings: ", self.toppings)
      print("Quantity: ", self.quantity)
      print("Price: ", self.price)

    def __init__(self, kind, quantityOrdered):
        super().__init__(kind, quantityOrdered)
        self.setToppings(kind)
        self.setPrice(kind)
        self.toppings = self.getToppings()
        self.price = self.getPrice()
