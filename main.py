# Furniture.py - This program calculates profits and sales prices for a furniture company.

itemName = "TV Stand"
retailPrice = 325.00
wholesalePrice = 200.00

# Calculate the profit
profit = retailPrice - wholesalePrice

# Calculate the sale price (25% off the retail price)
salePrice = retailPrice * 0.75

# Calculate the sale profit (profit from the sale price)
saleProfit = salePrice - wholesalePrice

# Output the results
print("Item Name: " + itemName)
print("Retail Price: $" + str(retailPrice))
print("Wholesale Price: $" + str(wholesalePrice))
print("Profit: $" + str(profit))
print("Sale Price: $" + str(salePrice))
print("Sale Profit: $" + str(saleProfit))