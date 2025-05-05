# Step 1: Define the ItemToPurchase class
class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0, item_description="none"):
        # --- Updated: Added item_description to constructor ---
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        # Method to print cost details
        total = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${int(self.item_price)} = ${int(total)}")

    def print_item_description(self):
        # Method to print item description
        print(f"{self.item_name}: {self.item_description}")


# Step 2: Define the ShoppingCart class
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        # --- Updated: Added cart_items list and initialized customer_name and current_date ---
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, modified_item):
        # --- Updated: Modify item attributes if values are provided ---
        found = False
        for item in self.cart_items:
            if item.item_name == modified_item.item_name:
                if modified_item.item_description != "none":
                    item.item_description = modified_item.item_description
                if modified_item.item_price != 0.0:
                    item.item_price = modified_item.item_price
                if modified_item.item_quantity != 0:
                    item.item_quantity = modified_item.item_quantity
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)

    def get_cost_of_cart(self):
        return sum(item.item_price * item.item_quantity for item in self.cart_items)

    def print_total(self):
        # --- Updated to match required OUTPUT SHOPPING CART format ---
        print("OUTPUT SHOPPING CART")
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        total_items = self.get_num_items_in_cart()
        print(f"Number of Items: {total_items}")
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                print(f"{item.item_name} {item.item_quantity} @ ${int(item.item_price)} = ${int(item.item_price * item.item_quantity)}")
            print(f"Total: ${int(self.get_cost_of_cart())}")

    def print_descriptions(self):
        # --- Updated to match required OUTPUT ITEMS' DESCRIPTIONS format ---
        print("OUTPUT ITEMS' DESCRIPTIONS")
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")


# Step 3: Define the print_menu function
def print_menu(cart):
    menu = """
MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
"""
    option = ""
    while option != "q":
        print(menu)
        option = input("Choose an option:\n").lower()

        if option == "a":
            print("ADD ITEM TO CART")
            name = input("Enter the item name:\n")
            description = input("Enter the item description:\n")
            price = float(input("Enter the item price:\n"))
            quantity = int(input("Enter the item quantity:\n"))
            item = ItemToPurchase(name, price, quantity, description)
            cart.add_item(item)

        elif option == "r":
            print("REMOVE ITEM FROM CART")
            name = input("Enter name of item to remove:\n")
            cart.remove_item(name)

        elif option == "c":
            print("CHANGE ITEM QUANTITY")
            name = input("Enter the item name:\n")
            quantity = int(input("Enter the new quantity:\n"))
            item = ItemToPurchase(name, 0.0, quantity)
            cart.modify_item(item)

        elif option == "i":
            cart.print_descriptions()

        elif option == "o":
            cart.print_total()

        elif option == "q":
            break

        else:
            print("Invalid option, please try again.")


# Step 4: Main program logic
if __name__ == "__main__":
    # --- Updated: Prompt for customer's name and today's date ---
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")

    print()
    print("Customer name:", customer_name)
    print("Today's date:", current_date)

    # Create ShoppingCart object with customer details
    customer_cart = ShoppingCart(customer_name, current_date)

    # Display menu
    print_menu(customer_cart)
