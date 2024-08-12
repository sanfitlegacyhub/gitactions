def add_item(inventory, item, quantity):
    """Function to add an item to the inventory."""
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity
    return inventory

def remove_item(inventory, item, quantity):
    """Function to remove an item from the inventory."""
    if item in inventory and inventory[item] >= quantity:
        inventory[item] -= quantity
        if inventory[item] == 0:
            del inventory[item]
    else:
        print(f"Cannot remove {quantity} of {item} - not enough in inventory.")
    return inventory

def display_inventory(inventory):
    """Function to display the current inventory."""
    print("\nCurrent Inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")
    print("\n")

def main():
    """Main function to run the inventory system."""
    inventory = {}

    # Adding items to the inventory
    inventory = add_item(inventory, "apple", 10)
    inventory = add_item(inventory, "banana", 5)
    inventory = add_item(inventory, "orange", 8)
    
    # Displaying the inventory
    display_inventory(inventory)

    # Removing items from the inventory
    inventory = remove_item(inventory, "banana", 2)
    inventory = remove_item(inventory, "apple", 15)  # Trying to remove more than available
    
    # Displaying the inventory again
    display_inventory(inventory)

if __name__ == "__main__":
    main()
