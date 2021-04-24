"""Superclass Stock
A general class from which all of the items for
sale at the hot dog stand are derived"""


class Stock:

    def __init__(self, kind, quantityOrdered):
        self.type = kind
        self.price = 0.0
        self.quantity = quantityOrdered

    def getPrice(self):
        return self.price

    def getType(self):
        return self.type

    def getQuantity(self):
        return self.quantity

    def getDetails(self):
        print(self.type, self.quantity, self.price)

