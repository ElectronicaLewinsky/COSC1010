# 09/09/24
# Python Program Sales Tax

# Display "Enter item_price Amount "
# Input item_price
# Display "state_sales_tax is 5% "
# Set state_sales_tax = 0.05
# Display "county_sales_tax is 2.5% "
# Set county_sales_tax = 0.025
# print("Your total cost is $",total_price,".",sep="")

county_tax_rate = 0.025
state_tax_rate = 0.05
tax_rate = county_tax_rate + state_tax_rate

item_price = float(input("Please enter the price of your item: "))
item_price = int(100 * item_price) # Item price in cents
total_price = item_price * (1 + tax_rate) # Total price in cents

print("Your Total Sales Cost is ${:0.2f}".format(total_price / 100.0))
print("Your Purchase Amount was ${:0.2f}".format(item_price / 100.0))
print("Your County Tax Rate was {:0.1f}%".format(int(county_tax_rate * 100)))
print("Your State Tax Rate was {:0.1f}%".format(int(state_tax_rate * 100)))
print("Your Total Tax Rate was {:0.1f}%".format(int(tax_rate * 100)))