# Defining Arrays To Store Product Data
product_ids = []
product_names = []
product_prices = []
product_categories = []

# Function To Load Data From The product_data.txt File
def load_data_from_file():
    with open('Data/product_data.txt', 'r') as file:
        for line in file:
            data = line.strip().split(', ')
            product_ids.append(int(data[0]))
            product_names.append(data[1])
            product_prices.append(float(data[2]))
            product_categories.append(data[3])

# Function To Insert A New Product
def insert_product():
    product_id = int(input("Enter ID: "))
    if product_id in product_ids:
        print("Product With This ID Already Exists.")
        return
    
    product_name = input("Enter Name: ")
    product_price = float(input("Enter Price: "))
    product_category = input("Enter Category: ")

    product_ids.append(product_id)
    product_names.append(product_name)
    product_prices.append(product_price)
    product_categories.append(product_category)

    print("Product Added Successfully.")

# Function To Update Product Details By ID
def update_product():
    product_id = int(input("Enter ID To Modify: "))
    if product_id in product_ids:
        index = product_ids.index(product_id)
        product_names[index] = input("Enter New Name: ")
        product_prices[index] = float(input("Enter New Price: "))
        product_categories[index] = input("Enter New Category: ")
        print("Product Modified Successfully.")
    else:
        print("Product ID Not Found.")

# Function To Delete Product By ID
def delete_product():
    product_id = int(input("Enter ID To Delete: "))
    if product_id in product_ids:
        index = product_ids.index(product_id)
        del product_ids[index]
        del product_names[index]
        del product_prices[index]
        del product_categories[index]
        print("Product Removed Successfully.")
    else:
        print("Product ID Not Found.")

# Function To Search For A Product By ID Or Name
def search_product():
    key = input("Enter ID Or Name To Search: ")
    found = False
    for i in range(len(product_ids)):
        if key == str(product_ids[i]) or key == product_names[i]:
            print("ID:", product_ids[i])
            print("Name:", product_names[i])
            print("Price:", product_prices[i])
            print("Category:", product_categories[i])
            found = True
    if not found:
        print("Product Not Found.")

# Bubble Sort function To Order Product Data By Price
def bubble_sort():
    n = len(product_prices)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if product_prices[j] > product_prices[j + 1]:
                product_prices[j], product_prices[j + 1] = product_prices[j + 1], product_prices[j]
                product_ids[j], product_ids[j + 1] = product_ids[j + 1], product_ids[j]
                product_names[j], product_names[j + 1] = product_names[j + 1], product_names[j]
                product_categories[j], product_categories[j + 1] = product_categories[j + 1], product_categories[j]

# Loading Data From The TextFile
load_data_from_file()

# Applying Bubble Sort To Order Product Data By Price
bubble_sort()

# Menu For User Interaction
while True:
    print("\nMenu:")
    print("1. View Products")
    print("2. Insert Product")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Search Product")
    print("6. Exit")

    choice = input("Enter An Option Number (1-6): ")

    if choice == '1':
        # View Products
        for i in range(len(product_ids)):
            print("\nID:", product_ids[i])
            print("Name:", product_names[i])
            print("Price:", product_prices[i])
            print("Category:", product_categories[i])

    elif choice == '2':
        # Adding Product
        insert_product()

    elif choice == '3':
        # Updating Product
        update_product()

    elif choice == '4':
        # Deleting Product
        delete_product()

    elif choice == '5':
        # Searching Product
        search_product()

    elif choice == '6':
        # Exiting The Program
        print("Exiting The Program. Goodbye!")
        break

    else:
        print("Invalid Option. Please Enter A Number From 1 to 6.")
