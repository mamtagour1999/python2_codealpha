# Hardcoded stock prices
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "AMZN": 3300
}

def calculate_investment(stock_name, quantity):
    """
    Calculate the investment value for the given stock and quantity.
    """
    price = STOCK_PRICES.get(stock_name.upper())
    if price:
        return price * quantity
    else:
        return None

def save_to_file(stock_name, quantity, total, filename="portfolio_summary.txt"):
    """
    Save the stock details to a text file.
    """
    with open(filename, "a") as file:
        file.write(f"{stock_name} | Quantity: {quantity} | Total: ${total}\n")
    print(f"Data saved to {filename}")

def main():
    stock_name = input("Enter stock symbol (e.g. AAPL, TSLA): ").strip()
    quantity_input = input("Enter quantity: ").strip()

    if not quantity_input.isdigit():
        print("Invalid quantity. Please enter a number.")
        return

    quantity = int(quantity_input)
    total = calculate_investment(stock_name, quantity)

    if total is not None:
        print(f"Total investment in {stock_name.upper()}: ${total}")
        
        save_option = input("Do you want to save the result to file? (yes/no): ").strip().lower()
        if save_option == "yes":
            save_to_file(stock_name.upper(), quantity, total)
    else:
        print("Stock symbol not found in our tracker.")

if __name__ == "__main__":
    main()
