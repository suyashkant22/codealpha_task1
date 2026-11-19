"""
- User inputs stock names and quantities.
- Prices come from a hardcoded dictionary.
- Displays total investment value and optionally saves it to a .txt or .csv file.
"""

import csv

# Hardcoded stock prices (USD)
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 125,
}


def get_portfolio():
    """Ask the user for stock names and quantities. Returns a list of holdings."""
    portfolio = []
    print("Available stocks:", ", ".join(f"{s} (${p})" for s, p in STOCK_PRICES.items()))
    print("Enter stock name and quantity. Type 'done' as the stock name to finish.\n")

    while True:
        name = input("Stock name: ").strip().upper()
        if name == "DONE":
            break
        if name not in STOCK_PRICES:
            print(f"  '{name}' is not available. Please choose from the list above.")
            continue

        qty_text = input(f"Quantity of {name}: ").strip()
        try:
            qty = int(qty_text)
            if qty <= 0:
                raise ValueError
        except ValueError:
            print("  Please enter a positive whole number for quantity.")
            continue

        price = STOCK_PRICES[name]
        portfolio.append({"stock": name, "quantity": qty, "price": price, "value": price * qty})
        print(f"  Added {qty} x {name} @ ${price} = ${price * qty}\n")

    return portfolio


def display_summary(portfolio):
    """Print a table of holdings and return the total investment."""
    total = sum(item["value"] for item in portfolio)
    print("\n" + "=" * 46)
    print(f"{'Stock':<10}{'Qty':>6}{'Price':>10}{'Value':>14}")
    print("-" * 46)
    for item in portfolio:
        print(f"{item['stock']:<10}{item['quantity']:>6}{item['price']:>10}{item['value']:>14}")
    print("-" * 46)
    print(f"{'Total Investment:':<26}{'$' + str(total):>20}")
    print("=" * 46)
    return total


def save_to_txt(portfolio, total, filename="portfolio.txt"):
    with open(filename, "w") as f:
        f.write("Stock Portfolio Summary\n")
        f.write("-" * 30 + "\n")
        for item in portfolio:
            f.write(f"{item['stock']}: {item['quantity']} x ${item['price']} = ${item['value']}\n")
        f.write("-" * 30 + "\n")
        f.write(f"Total Investment: ${total}\n")
    print(f"Saved to {filename}")


def save_to_csv(portfolio, total, filename="portfolio.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Stock", "Quantity", "Price", "Value"])
        for item in portfolio:
            writer.writerow([item["stock"], item["quantity"], item["price"], item["value"]])
        writer.writerow(["Total Investment", "", "", total])
    print(f"Saved to {filename}")


def main():
    portfolio = get_portfolio()
    if not portfolio:
        print("No stocks entered. Exiting.")
        return

    total = display_summary(portfolio)

    choice = input("\nSave result to file? (txt / csv / no): ").strip().lower()
    if choice == "txt":
        save_to_txt(portfolio, total)
    elif choice == "csv":
        save_to_csv(portfolio, total)
    else:
        print("Result not saved.")


if __name__ == "__main__":
    main()
