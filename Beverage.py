"""Sub Class Beverage creates all of the Beverage objects"""
from Stock import Stock

class Beverage(Stock):

    def getPrice(self):
        return self.price

    def __init__(self, quantityOrdered):
        super().__init__(quantityOrdered)
        self.price = 1.5 * float(quantityOrdered)


