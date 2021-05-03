"""Sub Class Chips creates all of the chips objects"""
from Stock import Stock

class Chips(Stock):

    def getPrice(self):
        return self.price

    def __init__(self, quantityOrdered):
        super().__init__(quantityOrdered)
        self.price = 1.00 * float(quantityOrdered)
