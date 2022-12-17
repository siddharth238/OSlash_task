

#The prices dictionary holds the prices for various items
prices = {
    "TSHIRT": 1000,
    "JACKET": 2000,
    "CAP": 500,
    "NOTEBOOK": 200,
    "PENS": 300,
    "MARKERS": 500
}



#The discounts dictionary holds the discounts for various items
discounts = {
    "TSHIRT": 10,
    "JACKET": 5,
    "CAP": 20,
    "NOTEBOOK": 20,
    "PENS": 10,
    "MARKERS": 5
}


#The max_quantities dictionary holds the maximum allowed quantities for various items
max_quantities = {
    "TSHIRT": 2,
    "JACKET": 2,
    "CAP": 2,
    "NOTEBOOK": 3,
    "PENS": 3,
    "MARKERS": 3
}

#The categories dictionary holds the categories for various items
categories = {
    "TSHIRT": "Clothing",
    "JACKET": "Clothing",
    "CAP": "Clothing",
    "NOTEBOOK": "Stationery",
    "PENS": "Stationery",
    "MARKERS": "Stationery"
}

#The shopping_cart dictionary holds the items and their quantities in the shopping cart
shopping_cart = {}


#The add_item function adds a specified quantity of a given item to the shopping cart
def add_item(item, quantity):
   
    if item in shopping_cart:
        shopping_cart[item] += quantity
         # If the item is already in the shopping cart, the quantity is added to the existing quantity
        
       
    else:
        
        shopping_cart[item] = quantity
         # If the item is not in the shopping cart, it is added with the specified quantity
    max_quantity = max_quantities[item]
    # The max_quantity variable holds the maximum allowed quantity for the given item
    if quantity > max_quantity:
        print("ERROR_QUANTITY_EXCEEDED")
        #If the quantity exceeds the maximum allowed quantity, an error message is printed
    else:
        print("ITEM_ADDED")
        # If the quantity does not exceed the maximum allowed quantity, a success message is printed


#The print_bill function calculates and prints the total discount, tax, and amount to be paid for the items in the shopping cart
def print_bill():
        
    total_discount = 0
    total_amount = 0
    # The total_discount variable holds the total discount applied to the items in the shopping cart
    # The total_amount variable holds the total amount of the items in the shopping cart, before any discounts are applied
    for item, quantity in shopping_cart.items():
        # The items and quantities in the shopping cart are iterated over
        price = prices[item]
        discount = discounts[item]
        category = categories[item]
        max_quantity = max_quantities[item]
        #price, discount, category and max_quantity are assigned to it item values
         
        if quantity <= max_quantity:    
        #checking if the quantity given is lesser to satify the condition
            item_total = price * quantity
            total_amount += item_total
            #incrementing the total amount with the total item price 
            if total_amount >= 1000:
                item_discount = (discount / 100) * item_total
                total_discount += item_discount
                total_amount -= item_discount
            #Checking if the total_amount is greater than or equal to 1000 so to satisfy the condition
            #incrementing the discount
            #decrementing the  total amount with the discount
    if total_amount >= 3000:
            additional_discount = (5 / 100) * total_amount              #if amount>3000 giving 5% discount
            total_discount += additional_discount
            total_amount -= additional_discount

    tax = (10 / 100) * total_amount                                #adding sales tax
    total_amount += tax

    print("TOTAL_DISCOUNT {:.2f}".format(total_discount))
    print("TOTAL_AMOUNT_TO_PAY {:.2f}".format(total_amount))
 
 
while True:
    command = input()
    if command.startswith("ADD_ITEM"):
        _, item, quantity = command.split()
        add_item(item, int(quantity))                         
    elif command == "PRINT_BILL":
        print_bill()
    elif command == "EXIT":
        break
