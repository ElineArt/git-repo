# Step 1 Response- Build the ItemToPurchase class with the required specifications.
class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0

    def print_item_cost(self):
        item_total_cost = self.item_quantity * self.item_price
        line = f"{self.item_name} {self.item_quantity} @ ${int(self.item_price)} = ${int(item_total_cost)}"
        print(line.center(60))

# Function to center text
def print_centered(text, width=60):
    print(text.center(width))

#Step 2 Response - prompts the user for two items and creates two objects of the ItemToPurchase class.
print("Item 1")
item1 = ItemToPurchase()
item1.item_name = input("Enter the item name: ")
item1.item_price = float(input("Enter the item price: "))
item1.item_quantity = int(input("Enter the item quantity: "))

print("\nItem 2")
item2 = ItemToPurchase()
item2.item_name = input("Enter the item name: ")
item2.item_price = float(input("Enter the item price: "))
item2.item_quantity = int(input("Enter the item quantity: "))

#Step3 Response - Add the costs of the two items together and output the total cost.
print()
print_centered("TOTAL COST")
print()
item1.print_item_cost()
print()
item2.print_item_cost()
total_cost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
print()
print_centered(f"Total: ${int(total_cost)}")
