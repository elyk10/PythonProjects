class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def productInfo(self):
        print(f"{self.name}: cost: {self.price} in stock: {self.quantity}")

    def quantityUpdate(self, quantity):
        self.quantity = quantity


def main():

    inventory = [Product("Toothbrush", 5.99, 10), Product("Toothpaste", 3.5, 20), Product("Floss", 1.00, 50)]

    loop = True

    while loop:
        newProduct = input("Would you like to add a new product (yes/no)?")
        if newProduct == "yes":
            name = input("What is the name of the product?")
            price = float(input("What is the cost of the product?"))
            quantity = int(input("How many of them are there?"))
            inventory.append(Product(name, price, quantity))

        else:
            loop = False

    totalValue = 0.0
    for i in inventory:
        totalValue += i.price * i.quantity

    print(f"The total value of the inventory is {totalValue}")


main()