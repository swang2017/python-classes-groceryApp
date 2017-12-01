class ShoppingList:
    def __init__(self,title):
        self.title = title
        self.items = []

    def addItem(self, item):
        self.items.append(item)


class GroceryItems:
    def __init__(self,title,price, quantity, barcode):
        self.title = title
        self.price = price
        self.quantity = quantity
        self.barcode = barcode


shoppinglist1 = ShoppingList('Fiesta')
shoppinglist1.addItem("Milk")
shoppinglist1.addItem("Soda")
shoppinglist1.addItem("Fish")

shoppinglist2 = ShoppingList('Walmart')
shoppinglist2.addItem("Paper")
shoppinglist2.addItem("Napkins")
shoppinglist2.addItem("Plate")
shoppinglist2.addItem("Chips")

shoppinglist3 = ShoppingList('Sams Club')
shoppinglist3.addItem("Chicken")
shoppinglist3.addItem("Beef")
shoppinglist3.addItem("Eggs")
shoppinglist3.addItem("Sugar")
shoppinglist3.addItem("Salt")
shoppinglist3.addItem("Pepper")
shoppinglist3.addItem("Honey")

print("Buy {0} from {1}".format(shoppinglist1.items, shoppinglist1.title))
print("Buy {0} from {1}".format(shoppinglist2.items, shoppinglist2.title))
print("Buy {0} from {1}".format(shoppinglist3.items, shoppinglist3.title))
