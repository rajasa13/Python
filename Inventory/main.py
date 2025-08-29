import json
import os

INVENTORY_FILE = 'inventory.json'

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
    item_id = input("Enter item ID: ")
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

