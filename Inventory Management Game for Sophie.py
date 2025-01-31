# Sophie's Boutique Inventory Management System
# This program will allow the user to manage the inventory by displaying, adding, updating, and removing items, as well as calculating the total value of the inventory.
# The program will display a menu with the following options:
# 1. Display Inventory
# 2. Add New Items
# 3. Update Existing Items
# 4. Remove Items
# 5. Calculate Total Inventory Value
# 6. Quit
# The user can choose an option by entering the corresponding number. The program will then perform the selected action and display the results.
# The inventory will be stored as a dictionary with the item name as the key and the quantity and price as the values.
# The program will use a while loop to keep displaying the menu until the user chooses to quit.
# The program will handle invalid choices by displaying an error message and allowing the user to choose again.
# The program will calculate the total value of the inventory by multiplying the quantity and price of each item and summing the results.

# first creating a dictionary to store the inventory items
inventory = {
    "Dress": {"quantity": 10, "price": 29.99}, #dress is the item and the quantity and price are the details of the item which is inside a dictionary
    "Shoes": {"quantity": 35, "price": 49.99}, #shoes is the item and the quantity and price are the details of the item which is inside a dictionary
    "Hat": {"quantity": 20, "price": 9.99},  #hat is the item and the quantity and price are the details of the item which is inside a dictionary
    "Shirt": {"quantity": 15, "price": 10.99}, #shirt is the item and the quantity and price are the details of the item which is inside a dictionary
    "Trouser": {"quantity": 25, "price": 19.99}, #trouser is the item and the quantity and price are the details of the item which is inside a dictionary
    "Jacket": {"quantity": 18, "price": 59.99}, #jacket is the item and the quantity and price are the details of the item which is inside a dictionary
}

# displaying menu options using while loop so that the user can keep using the program until they choose a valid option
while True:
    print("----- Sophie's Boutique -----")
    print("------------------------")
    print("1. Display Inventory")
    print("------------------------")
    print("2. Add New Items")
    print("------------------------")
    print("3. Update Existing Items")
    print("------------------------")
    print("4. Remove Items")
    print("------------------------")
    print("5. Calculate Total Inventory Value")
    print("------------------------")
    print("6. Quit")
    print("------------------------")
    
    
    #getting user choice and storing it in a variable before using if statements to perform their selected action
    choice = input("Choose an option: ")
    
    #displaying inventory items
    if choice == '1':
        print("\n----- Inventory -----")
        for item, details in inventory.items():     #item is the key and details is the value from the dictionary
            print(f"{item}: Quantity: {details['quantity']}, Price: £{details['price']:.2f}") #displaying the item, quantity and price
        print("---------------------\n")

    #adding new item to inventory 
    elif choice == '2':
        item = input("Enter the name of the item: ")
        if item in inventory:
            print("Item already exists. Please use the update option in the main menu to modify it.")
            continue
        quantity = int(input("Enter the quantity: "))
        price = float(input("Enter the price: £"))
        inventory[item] = {"quantity": quantity, "price": price} #the brackets are used to store the quantity and price in a dictionary
        print(f"{item} has been added to inventory.")

    #updating existing item in inventory
    elif choice == '3':
        item = input("Enter the name of the item to update: ")
        if item not in inventory:
            print("Item not found in inventory.")
            continue
        quantity = int(input("Enter the new quantity: "))
        price = float(input("Enter the new price: £"))
        inventory[item] = {"quantity": quantity, "price": price}
        print(f"{item} updated in inventory.")

    #removing items from inventory
    elif choice == '4':
        item = input("Enter the name of the item to remove: ")
        if item not in inventory:
            print("Item not found in inventory.")
            continue
        del inventory[item]
        print(f"{item} removed from inventory.")

    # Calculating the total inventory value
    elif choice == '5':
        total_value = sum(details['quantity'] * details['price'] for details in inventory.values()) #this gets the quantity and price of each item and multiplies them to get the total value
        print(f"Total inventory value: £{total_value:.2f}")

    # Quiting the program
    elif choice == '6':
        print("User logged out.")
        break

    # taking care of invalid choices
    else:
        print("Invalid choice. Please select a valid option.")
