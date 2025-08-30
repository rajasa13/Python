import json
import os

# Path of the current inventory file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# JSON file inside the same folder as main.py
INVENTORY_FILE = os.path.join(BASE_DIR, 'inventory.json')

# Load inventory from file
def load_inventory():
    if os.path.exists(INVENTORY_FILE):
        with open(INVENTORY_FILE, 'r') as file:
            return json.load(file)
    return {}

# Save inventory to file
def save_inventory(inventory):
    with open(INVENTORY_FILE, 'w') as file:
        json.dump(inventory, file, indent=4)

# Add a new item to the inventory
def add_item(inventory):
    item_id = int(input("Enter item ID: "))
    if item_id in inventory:
        print("Item ID already exists!")
        return
    name = input("Enter item name: ")
    unit = input("Enter item unit (e.g., kg, pcs): ")
    quantity = int(input("Enter item quantity: "))
    inventory[item_id] = {'name': name, 
                          'unit': unit, 
                          'quantity': quantity}
    print("Item added successfully!")

# Record incoming goods
def incoming_goods(inventory):
    item_id = int(input("Enter item ID: "))
    if item_id not in inventory:
        print("Item not found!")
        return
    qty = int(input("Enter incoming quantity: "))
    inventory[item_id]["quantity"] += qty
    print("Incoming goods recorded!")

# Record outgoing goods
def outgoing_goods(inventory):
    item_id = int(input("Enter item ID: "))
    if item_id not in inventory:
        print("Item not found!")
        return
    qty = int(input("Enter outgoing quantity: "))
    if qty > inventory[item_id]["quantity"]:
        print("Not enough stock!")
        return
    inventory[item_id]["quantity"] -= qty
    print("Outgoing goods recorded!")

# Show inventory
def show_inventory(inventory):
    print("\n--- INVENTORY LIST ---")
    if not inventory:
        print("Inventory is empty.")
        return
    for item_id in sorted(inventory.keys()): # Sort by item ID numerically
        data = inventory[item_id]
        print(f"{item_id}: {data['name']} - {data['quantity']} - {data['unit']}")

# Delete item
def delete_item(inventory):
    item_id = input("Enter item ID to delete: ")
    if item_id not in inventory:
        print("Item not found!")
        return
    confirm = input(f"Are you sure you want to delete '{inventory[item_id]['name']}'? (y/n): ")
    if confirm == 'y':
        del inventory[item_id]
        print("Item deleted successfully!")
    else:
        print("Delete cancelled.")

def main():
    inventory = load_inventory()
    while True:
        print("\n1. Add Item")
        print("2. Record Incoming Goods")
        print("3. Record Outgoing Goods")
        print("4. Show Inventory")
        print("5. Delete Item")
        print("6. Exit")
        choice = input("Choose: ")

        if choice == "1":
            add_item(inventory)
        elif choice == "2":
            incoming_goods(inventory)
        elif choice == "3":
            outgoing_goods(inventory)
        elif choice == "4":
            show_inventory(inventory)
        elif choice == "5":
            delete_item(inventory)
        elif choice == "6":
            save_inventory(inventory)
            print("Inventory saved. Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()