class BakeryItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - ${self.price:.2f} ({self.quantity} available)"

class BakeryManagement:
    def __init__(self):
        self.inventory = []

    def add_item(self, name, price, quantity):
        item = BakeryItem(name, price, quantity)
        self.inventory.append(item)

    def display_inventory(self):
        if not self.inventory:
            print("Inventory is empty.")
        else:
            for idx, item in enumerate(self.inventory):
                print(f"{idx + 1}. {item}")

    def place_order(self, item_index, order_quantity):
        if 0 <= item_index < len(self.inventory):
            item = self.inventory[item_index]
            if item.quantity >= order_quantity:
                item.quantity -= order_quantity
                print(f"Order placed for {order_quantity} of {item.name}")
                print(f"Total cost: ${item.price * order_quantity:.2f}")
            else:
                print(f"Insufficient quantity for {item.name}")
        else:
            print("Invalid item selection")

def main():
    bakery = BakeryManagement()
    
    while True:
        print("\n--- Bakery Management System ---")
        print("1. Add item")
        print("2. Display inventory")
        print("3. Place order")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            quantity = int(input("Enter item quantity: "))
            bakery.add_item(name, price, quantity)
            print(f"Item '{name}' added to inventory.")
        
        elif choice == '2':
            print("\n--- Inventory ---")
            bakery.display_inventory()
        
        elif choice == '3':
            bakery.display_inventory()
            if bakery.inventory:  # Check if inventory is not empty
                try:
                    item_index = int(input("Enter the item number to order: ")) - 1
                    order_quantity = int(input("Enter the quantity to order: "))
                    bakery.place_order(item_index, order_quantity)
                except ValueError:
                    print("Please enter valid numbers.")
        
        elif choice == '4':
            print("Exiting the Bakery Management System.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
