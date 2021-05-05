from node import Node
from linkedqueue import LinkedQueue
from HotDog_Edited import HotDog
from Beverage import Beverage
from Chips import Chips

class HotDogStand(LinkedQueue):
    def __init__(self, sourceCollection=None):
        LinkedQueue.__init__(self, sourceCollection)

    def displayActions(self):
        try:
            print("What would you like to do?")
            print("1. Take order")
            print("2. Display current order")
            print("3. Take payment")
            print("4. Serve order")
            print("5. Display all menu items")
            print("6. Exit")
            choice = int(input("Please enter a number from the menu above:"))

            if choice == 1:
                self.takeOrder()
            elif choice == 2:
                self.displayCurrentOrder()
            elif choice == 3:
                self.takePayment()
            elif choice == 4:
                self.serve()
            elif choice == 5:
                self.displayMenuItems()
            elif choice == 6:
                print("Bye")
        except:
            print("Invalid input, please select a number from the menu")
            self.goBackToMainMenu()

    def takeOrder(self):
        orderList = []
        
        hotdogOrder = self.takeHotDogOrder()
        orderList.append(hotdogOrder)
        drinkOrder = self.takeBeverageOrder()
        orderList.append(drinkOrder)
        chipsOrder = self.takeChipOrder()
        orderList.append(chipsOrder)
        orderNode = Node(orderList)
        self.add(orderNode)
        self.goBackToMainMenu()

    def takeHotDogOrder(self):
        wantAHotdog = input("Order a hotdog? Enter Y for yes or N for no")
        if wantAHotdog == 'Y' or wantAHotdog =='y':
            hotdogQty = input("How many hotdogs would you like? ")
            hotdogs = HotDog(hotdogQty)
            hotdogList = ["hotdog", "qty: " + str(hotdogs.quantity), hotdogs.price]
            return hotdogList

        elif wantAHotdog != 'Y' and wantAHotdog !='y' and \
                wantAHotdog !='N' and wantAHotdog !='n':
            print("Invalid input, enter 'Y' for yes or 'N' for no\n")
            wantAHotdog = input("Order a hotdog? Enter Y for yes or N for no")
            if wantAHotdog == 'Y' or wantAHotdog == 'y':
                hotdogQty = input("How many hotdogs would you like? ")
                hotdogs = HotDog(hotdogQty)
                hotdogList = ["hotdog", "qty: " + str(hotdogs.quantity), hotdogs.price]
                return hotdogList

        elif wantAHotdog == 'N' or wantAHotdog == 'n':
            hotdogList = ["hotdog", "qty: 0", 0.0]
            return hotdogList

    def takeBeverageOrder(self):
        wantADrink = input("Want a drink? Enter Y for yes or N for no")
        if wantADrink == 'Y' or wantADrink == 'y':
            drinkQty = input("How many drinks would you like? ")
            drinks = Beverage(drinkQty)
            drinkList = ["beverage", "qty: " + str(drinks.quantity),
                          drinks.price]
            return drinkList

        elif wantADrink != 'Y' and wantADrink != 'y' and \
                wantADrink != 'N' and wantADrink != 'n':
            print("Invalid input, enter 'Y' for yes or 'N' for no")
            wantADrink = input("Want a drink? Enter Y for yes or N for no")
            if wantADrink == 'Y' or wantADrink == 'y':
                drinkQty = input("How many drinks would you like? ")
                drinks = Beverage(drinkQty)
                drinkList = ["beverage", "qty: " + str(drinks.quantity),
                             drinks.price]
                return drinkList
            
        elif wantADrink == 'N' or wantADrink == 'n':
            drinkList = ["beverage", "qty: 0", 0.0]
            return drinkList

    def takeChipOrder(self):
        wantChips = input("Want some chips? Enter Y for yes or N for no")
        if wantChips == 'Y' or wantChips == 'y':
            chipQty = input("How many bags of chips would you like? ")
            chips = Chips(chipQty)
            chipsList = ["chips", "qty:" + str(chips.quantity),
                          chips.price]
            return chipsList
            
        elif wantChips != 'Y' and wantChips != 'y' and \
                wantChips != 'N' and wantChips != 'n':
            print("Invalid input, enter 'Y' for yes or 'N' for no")
            wantChips = input("Want some chips? Enter Y for yes or N for no")
            if wantChips == 'Y' or wantChips == 'y':
                chipQty = input("How many bags of chips would you like? ")
                chips = Chips(chipQty)
                chipsList = ["chips", "qty:" + str(chips.quantity),
                             chips.price]
                return chipsList

        elif wantChips == 'N' or wantChips == 'n':
            chipsList = ["chips", "qty: 0", 0.0]
            return chipsList

    def displayCurrentOrder(self):
        if self.isEmpty() == False:
            print(self.peek().data)
            self.goBackToMainMenu()
        else:
            print("The queue is empty\n")
            self.goBackToMainMenu()

    def takePayment(self):
        if self.isEmpty():
            print("There are no orders")
            self.goBackToMainMenu()
        else:
            priceList = []
            for order in self.peek().data:
                priceList.append(order[2])

            total = 0
            for price in priceList:
                total += price
            print("The total is $%.2f"%total)
            cashGiven = float(input("Enter amount of cash paid by customer:"))
            change = cashGiven - total
            print("Cash back: $%.2f"%change + "\n")
            self.goBackToMainMenu()

    def serve(self):
        print("First order: " + str(self.peek().data))
        print("Size of order queue: " + str(self.size))
        self.pop()
        if (self.isEmpty()):
            print("There are no more orders")
        else:
            print("New first order: " + str(self.peek().data))
        print("Size of order queue after serving up order: " + str(self.size) + "\n")
        self.goBackToMainMenu()

    def displayMenuItems(self):
        print("Hotdogs: $4.00")
        print("Drinks: $1.50")
        print("Chips: $1.00")
        self.goBackToMainMenu()

    def goBackToMainMenu(self):
        choice = input("Go back to main menu? Enter 'Y' for yes or 'N' for no")
        if choice == 'Y' or choice == 'y':
            self.displayActions()
        elif choice == 'N' or choice == 'n':
            print("Bye")
        else:
            print("Invalid input, enter 'Y' for yes or 'N' for no")
            self.goBackToMainMenu()
