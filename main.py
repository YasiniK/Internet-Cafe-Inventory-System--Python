from prettytable import PrettyTable
import random
from datetime import datetime

products_lis = []  # create an empty list to hold all the products
dealers = {}  # create an empty dictionary to store dealer details
random_dealers = {}  # create an empty dictionary to store random dealers
product = {}  # create an empty dictionary to store product details


def confirm():
    while True:
        choice_a = input('''\n           
    ___________________________________________________
    |>Type R to return to main menu 
    |>Type ESC to exit
    |__________________________________________________
    |>Enter your command here: ''')
        if choice_a.upper() == "R":
            break  # return to the main menu
        elif choice_a.upper() == "ESC":
            exit()  # exit the program
        else:
            print("Invalid choice. Please try again.")
        return ()


def save_txt(products_lis):  # This function is to save the product details into a text file
    # if there are no products in the list, return to main menu
    if len(products_lis) == 0:
        return ()

    item_table = PrettyTable()  # create a table using PrettyTable
    item_table.field_names = ["Code", "Name", "Brand", "Price", "Quantity", "Category",
                              "Purchased Date"]  # define table headers
    for product in products_lis:
        # add each product as a new row to the item_table
        item_table.add_row([product["Code"], product["Name"], product["Brand"], product["Price"], product["Quantity"],
                            product["Category"], product["Purchased Date"]])

        with open("output.txt", "w") as f:  # write the item_table to a text file named "output.txt"
            f.write(str(item_table))


def add_product():  # This function is used for getting products details from the user
    # get item code
    while True:
        item_code = input("Enter item code: ")
        if item_code == "":
            print("Item code cannot be empty. Please enter a valid item code.")
            continue

        # Check if item code already exists in products_lis
        for product in products_lis:
            if product['Code'] == item_code:
                print(f"Item code {item_code} already exists. Please enter a unique item code.")
                break
        else:
            break

    # get product name
    while True:
        item_name = input("Enter item name: ")
        if item_name == "":
            print("Item name cannot be empty. Please enter a valid item name.")
            continue
        break

    # get product brand
    while True:
        item_brand = input("Enter item brand: ")
        if item_brand == "":
            print("Item brand cannot be empty. Please enter a valid item brand.")
            continue
        break

    # ask user for price input until a valid float value is entered
    while True:
        try:
            price = float(input("Enter price: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for price.")

    # ask user for quantity input until a valid int is entered
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for quantity.")

    # get product category
    while True:
        category = input("Enter category: ")
        if category == "":
            print("Category cannot be empty. Please enter a valid category.")
            continue
        break

    # ask user for purchased date input until a valid date is entered
    while True:
        purchased_date = input("Enter a date in the format YYYY-MM-DD: ")
        try:
            datetime.strptime(purchased_date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please enter a date in the format YYYY-MM-DD.")

    # product details are saved as a dictionary
    product = {
        "Code": item_code,
        "Name": item_name,
        "Brand": item_brand,
        "Price": f'{price}/=',
        "Quantity": quantity,
        "Category": category,
        "Purchased Date": purchased_date,
        "sub total": price * quantity
    }
    products_lis.append(product)  # add the product to the list of products
    print("\n""====================Item added successfully!=========================")


def delete_product(products_lis):  # This function use to delete details of an item, searching by item code
    if len(products_lis) == 0:
        print("\nNo items to delete.")
        return ()
    item_code = input("Enter the item code to be deleted: ")
    item_found = False  # variable to keep track of whether the item was found or not
    for product in products_lis:
        if product["Code"] == item_code:
            products_lis.remove(product)
            print("Product deleted successfully")
            save_txt(products_lis)
            item_found = True
            break
    if not item_found:
        print("Item code not found.")


def update_product(product, category):  # This function use to update product details, searching by item_code
    if category == "NAME":
        product["Name"] = input("Enter new name: ")  # getting the new name for update
    elif category == "BRAND":
        product["Brand"] = input("Enter new brand: ")  # getting the new brand for update
    elif category == "PRICE":
        while True:
            try:
                new_price = float(input("Enter new price: "))  # getting the new price for update
                product["Price"] = new_price
                product["sub total"] = product["Price"] * product["Quantity"]
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")  # checking validity
                continue
    elif category == "QUANTITY":
        while True:
            try:
                new_quantity = int(input("Enter new quantity: "))  # getting the new quantity for update
                product["Quantity"] = new_quantity
                product["sub total"] = product["Price"] * product["Quantity"]
                break
            except ValueError:
                print("Invalid input. Please enter a valid number for quantity.")  # checking validity

    elif category == "CATEGORY":
        product["Category"] = input("Enter new category: ")  # getting the new category for update
    elif category == "DATE":
        while True:
            purchased_date = input("Enter a date in the format YYYY-MM-DD: ")  # getting the new date for update
            try:
                datetime.strptime(purchased_date, "%Y-%m-%d")
                break
            except ValueError:
                print("Invalid date format. Please enter a date in the format YYYY-MM-DD.")  # checking validity
    else:
        print("Invalid input.")


def print_details():  # This function use to print details of randomly selected dealers
    for name, info in dealers.items():
        if name in random_dealers:  # Check if the name is in the "random_dealers" list
            print(f"\nDealer: {name}")
            print(f"Location: {info['location']}")
            print(f"Contact: {info['contact']}")
            # Create a table using PrettyTable and print it
            d_items = PrettyTable()
            d_items.field_names = ["Name", "Brand", "Price", "Quantity"]  # Define the field names for the table
            for item in items:
                d_items.add_row([item["name"], item["brand"], item["price"], item["quantity"]])
            print(d_items)


while True:

    command = input('''    
    |_____________________________Welcome to the Item Management System!______________________|

    |>Type AID for adding item details.
    |>Type DID for deleting item details.
    |>Type UID for updating item details.
    |>Type VID for viewing the items table and print the current total.
    |>Type SID for saving the item details to the text file at any time.
    |>Type SDD for selecting four dealers randomly from a file.
    |>Type VRL for displaying all the details of the randomly selected dealers.
    |>Type LDI for display the items of the given dealer.
    |>Type ESC to exit the program. 
    --------------------------------------------------------------------------
    Enter your command here: ''')

    if command.upper() == "AID":  # converting the input to upper case
        add_product()  # call the add_product function
        while True:
            answer = input("Do you want to add another item? (yes or no): ")
            if answer.lower() == "yes":
                add_product()  # call the add_product function
            elif answer.lower() == "no":
                confirm()  # call the confirm function
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

    elif command.upper() == "DID":  # converting the input to upper case
        delete_product(products_lis)  # call the delete_product function
        confirm()

    elif command.upper() == "UID":  # converting the input to upper case
        if len(products_lis) == 0:
            print("\n no items to update")
            confirm()
            continue

        item_code = input("Enter item code to update: ")  # get the item_code to update the details
        for product in products_lis:
            if product["Code"] == item_code:  # checking the item_code
                print(f'You can update the product: "{product["Name"]}"')

                while True:
                    category = input(
                        "Which category would you like to update? (name/brand/price/quantity/category/date): ").upper()
                    update_product(product, category)
                    choice = input(
                        "Do you want to update another category? (Y/N)").upper()  # Convert input to uppercase

                    if choice == "Y":
                        continue
                    else:
                        break

                print("\n                   Item updated successfully.")
                confirm()

                break
        else:
            print("\n Item not found.")
            confirm()


    elif command.upper() == "VID":  # converting the input to upper case

        # Sort the list of products_lis by descending order using sort algorithm
        n = len(products_lis)  # Get the length of the list
        for i in range(n):
            max_idx = i  # Set the maximum index to the current index
            for j in range(i + 1, n):
                if int(products_lis[j]['Code']) > int(
                        products_lis[max_idx]['Code']):  # If the current item is greater than the maximum item

                    max_idx = j  # Set the maximum index to the index of the current item
            products_lis[i], products_lis[max_idx] = products_lis[max_idx], products_lis[
                i]  # Swap the current item with the maximum item

        # Create a table using PrettyTable and print it
        item_table = PrettyTable()
        item_table.field_names = ["Code", "Name", "Brand", "Price", "Quantity", "Category", "Purchased Date"]
        for product in products_lis:
            item_table.add_row(
                [product["Code"], product["Name"], product["Brand"], product["Price"], product["Quantity"],
                 product["Category"], product["Purchased Date"]])
        print(item_table)

        # Calculate and print the total cost of all products
        total = 0
        for product in products_lis:
            total += product["sub total"]
        print(f'total cost is -: {total} /=')
        print("==========*Table created successfully!*===========")

        # Ask the user to save the table to a text file or return to the main menu or exit
        while True:
            choice_v = input('''\n            
        _______________________________________
        |>Type S to save this table to TXT file
        |>Type R to return to main menu 
        |>Type ESC to exit
        |______________________________________
        |>Enter your command here: ''')
            if choice_v.upper() == "R":
                break
            elif choice_v.upper() == "ESC":
                exit()
            elif choice_v.upper() == "S":
                save_txt(products_lis)
                print("==========*Item details saved to the Text File successfully!*===========")

    elif command.upper() == "SID":  # converting the input to upper case
        save_txt(products_lis)
        if len(products_lis) != 0:  # check if there are products in the products_lis list
            print("==========*Item details saved to the Text File successfully!*===========")
            confirm()  # call the confirm function

    with open('dealers.txt', 'r') as f:  # open the file "dealers.txt"
        data = f.readlines()  # read all the lines in the file and store them as a list called "data"
        data = [line.strip().split(',') for line in data]  # split each line into a list of values using ','

    n = len(data)  # find the length of the "data" list
    for i in range(n):
        max_idx = i  # Set the current index as the maximum index
        for j in range(i + 1, n):
            if data[j][1] < data[max_idx][1]:
                max_idx = j
        data[i], data[max_idx] = data[max_idx], data[i]

    data_sorted_str = [','.join(row) for row in data]
    with open('dealers_sorted.txt', 'w') as f:  # Open a new file "dealers_sorted.txt"
        f.write('\n'.join(data_sorted_str))

    with open("dealers_sorted.txt") as f:  # Open the file "dealers_sorted.txt"
        for line in f:
            fields = line.strip().split(",")  # Split each line using ','

            # Get the dealer's name, location, and contact
            name = fields[0]
            location = fields[1]
            contact = fields[2]

            items = []  # Create a list to store the dealer's items
            for i in range(3, len(fields), 4):
                # Create a dictionary for each item
                item = {"name": fields[i], "brand": fields[i + 1], "quantity": int(fields[i + 2]),
                        "price": int(fields[i + 3])}
                items.append(item)  # Append the item to the items list

            # Create a dictionary for the dealer
            dealers[name] = {"location": location, "contact": contact, "items": items}

    if command.upper() == "SDD":  # converting the input to upper case
        dealers_list = list(
            dealers.keys())  # The variable dealers_list is assigned a list of keys from the dealers dictionary
        random_dealers = random.sample(dealers_list, 4)
        print("Random 4 dealers: ")  # print 4 random dealers
        for dealer in random_dealers:
            print(dealer)
        while True:
            choice_s = input('''_______________________________________
|>Type R to return to main menu 
|>Type ESC to exit
|>Type VRL to view full details
|______________________________________
|>Enter your command here: ''')
            if choice_s.upper() == "R":
                break  # return to the main menu
            elif choice_s.upper() == "ESC":
                exit()  # exit the program
            elif choice_s.upper() == "VRL":
                print_details()
            else:
                print("Invalid choice. Please try again.")

    elif command.upper() == "VRL":  # converting the input to upper case
        print_details()  # call the print details function
        confirm()

    elif command.upper() == "LDI":  # converting the input to upper case
        print(f'selected dealers are: {random_dealers}')  # Print the names of the randomly selected dealers
        dealer_name = input(f'Enter dealer name: ')  # Ask the user to enter the name of a dealer
        if dealer_name in dealers:  # Check if the dealer exists in the "dealers" dictionary
            if dealer_name in random_dealers:  # Check if the dealer is one of the randomly selected dealers
                dealer_info = dealers[dealer_name]
                # Create a table using PrettyTable and print it
                d_items = PrettyTable()
                d_items.field_names = ["Name", "Brand", "Price", "Quantity"]
                for item in items:
                    d_items.add_row([item["name"], item["brand"], item["price"], item["quantity"]])
                print(d_items)
            else:
                print("this is not a selected dealer")
        else:
            print("dealer doesn't exist")
            confirm()

    elif command.upper() == "ESC":  # converting the input to upper case
        quit()  # Exit the program
