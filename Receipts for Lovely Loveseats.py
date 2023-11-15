# create variable for loveseat description
lovely_loveseat_description = """
Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.
"""
# create a variable for lovely_loveseat_price and set to 254.00
lovely_loveseat_price = 254.00
# create a variable for settee description
stylish_settee_description = """
Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.
"""
# create and set a variable for settee price
stylish_settee_price = 180.50
# create a variable for luxurious lamp description
luxurious_lamp_description = """
Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.
"""
# create a variable luxurious_lamp_price and assign float 
luxurious_lamp_price = 52.15
# create and assign variable sales_tax
sales_tax = .088
# create and define a variable customer_one_total for a running tally of expenses
customer_one_total = 0
# create a variable customer_one_itemization to keep a list of the descriptions of things they're purchasing
customer_one_itemization = ""
# purchased the Lovely Loveseat and add it to customer_one_total
customer_one_total += lovely_loveseat_price
# add the description of the lovely loveseat
customer_one_itemization += lovely_loveseat_description
# add the price of the luxurious lamp to the customer one's total
customer_one_total += luxurious_lamp_price
# update the Customer's itemization with luxurious lamp description
customer_one_itemization += luxurious_lamp_description
# create a variable customer_one_tax and set it equal to customer_one_total times sales_tax
customer_one_tax = customer_one_total * sales_tax
# add sales tax to the customer's total cost
customer_one_total += customer_one_tax
# start printing the reciept, print heading
print("Customer One Items:")
print(customer_one_itemization)
# Print total cost
print("Customer One Total:")
print(customer_one_total)