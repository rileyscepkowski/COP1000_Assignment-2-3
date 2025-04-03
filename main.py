import unittest

# Furniture.py - This program calculates profits and sales prices for a furniture company.

itemName = "TV Stand"
retailPrice = 325.00
wholesalePrice = 200.00

# Function to calculate profit
def calculate_profit(retailPrice, wholesalePrice):
    return retailPrice - wholesalePrice

# Function to calculate sale price (25% discount on retail price)
def calculate_sale_price(retailPrice):
    return retailPrice * 0.75

# Function to calculate sale profit (sale price - wholesale price)
def calculate_sale_profit(salePrice, wholesalePrice):
    return salePrice - wholesalePrice

# Unit tests
class TestFurnitureCalculations(unittest.TestCase):

    def test_profit_calculation(self):
        # Test for profit calculation
        profit = calculate_profit(retailPrice, wholesalePrice)
        self.assertEqual(profit, 125.00)  # Expected profit is 325 - 200 = 125

    def test_sale_profit_calculation(self):
        # Test for sale price and sale profit calculation
        salePrice = calculate_sale_price(retailPrice)
        saleProfit = calculate_sale_profit(salePrice, wholesalePrice)
        self.assertEqual(saleProfit, 43.75)  # Expected sale profit is (243.75 - 200 = 43.75)

# Main program logic
def main():
    profit = calculate_profit(retailPrice, wholesalePrice)
    salePrice = calculate_sale_price(retailPrice)
    saleProfit = calculate_sale_profit(salePrice, wholesalePrice)

    # Output the results
    print("Item Name: " + itemName)
    print("Retail Price: $" + str(retailPrice))
    print("Wholesale Price: $" + str(wholesalePrice))
    print("Profit: $" + str(profit))
    print("Sale Price: $" + str(salePrice))
    print("Sale Profit: $" + str(saleProfit))

if __name__ == "__main__":
    # If running unit tests
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

    # If running the main program logic
    main()