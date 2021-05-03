"""Superclass Stock
A general class from which all of the items for
sale at the hot dog stand are derived"""


class Stock:

    def __init__(self, quantityOrdered):
        self.price = 0.0
        self.quantity = quantityOrdered

    def getPrice(self):
        return self.price

    def getQuantity(self):
        return self.quantity
