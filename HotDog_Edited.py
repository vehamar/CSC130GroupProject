"""Sub Class HotDog creates all of the hot dog objects"""
from Stock_Edited import Stock

class HotDog(Stock):

    def getPrice(self):
        return self.price

    def __init__(self, quantityOrdered):
        super().__init__(quantityOrdered)
        self.price = 4.00 * float(quantityOrdered)
