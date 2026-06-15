prices = {"Apple": 180, "TSLA": 250, "MSFT": 300, "GOOGLE": 2800}

total_investment = 0

print("Welcome to Stock Portfolio Tracker!")
print("Available stocks:", ", ".join(prices.keys()))

while True:
    stock = input("Enter stock symbol (or 'quit' to finish): ").upper()
    if stock == "QUIT":
        break
    if stock not in prices:
        print("Stock not found. Try again.")
        continue

    quantity = int(input(f"Enter quantity of {stock}: "))
    investment = prices[stock] * quantity
    total_investment += investment
    print(f"{stock}: {quantity} × {prices[stock]} = {investment}")

print("\nTotal Investment Value:", total_investment)
save = input("Save result to file? (y/n): ").lower()
if save == "y":
    with open("portfolio.txt", "w") as f:
        f.write(f"Total Investment Value: {total_investment}\n")
    print("Result saved to portfolio.txt")
