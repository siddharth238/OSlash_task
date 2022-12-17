 

add_item(item, quantity) is a function that adds a specified quantity of a given item to the shopping cart. 
If the item is already in the shopping cart, the quantity is added to the existing quantity. If the item is not in the shopping cart, 
it is added with the specified quantity. 
If the quantity exceeds the maximum allowed quantity for the item, an error message is printed. Otherwise, a success message is printed.



print_bill() is a function that calculates and prints the total discount, tax, and amount to be paid for the items in the shopping cart. 
The function iterates over the items and quantities in the shopping cart and calculates the total amount before discounts are applied. 
If the total amount is greater than or equal to 1000, the function applies the discount specified in the discounts dictionary to each item. 
If the total amount after applying the discounts is still greater than or equal to 3000, the function applies an additional 5% discount to the total amount. 
Finally, the function adds a 10% sales tax to the total amount and prints the total discount, total amount to be paid, and the amount of tax.
