"""This is the main file I used to test the code in the classes.
    The sample menu doesn't do anything right now, it just explains
    the toppings and types in the HotDog class."""

from Stock import Stock
from HotDog import HotDog

def main():
    choice = 0
    displayMenu()
    myOrder = orderHotDog(choice)
    myOrder.getDetails()



def displayMenu():
    print("Welcome to Talon's Hot Dog Stand")
    print("Hot Dogs: $4.00")
    print("1. Classic Dog: Ketchup and Mustard")
    print("2. Atlanta Dog: Chili, Slaw, Mustard")
    print("3. New York Dog: Onions, Spicy Mustard")
    print("4. Chicago Dog: Mustard, Relish, Onion, Pickle, Pepper, Tomato")
    print("5. Chili Dog: Chili, Onions, Cheese")
    print("6. Talon Dog: Chef's surprise")
    print("Enter any other number for a plain hot dog")
    choice = input("Enter the number of the customer's choice: ")
    return choice

def orderHotDog(choice):
    if choice == 1:
        kind = "Classic Dog"
    elif choice == 2:
        kind = "Atlanta Dog"
    elif choice == 3:
        kind = "New York Dog"
    elif choice == 4:
        kind = "Chicago Dog"
    elif choice == 5:
        kind = "Chili Dog"
    elif choice == 6:
        kind = "Talon Dog"
    else:
        kind = "Plain"

    return kind

if __name__ == "__main__":
    main()
