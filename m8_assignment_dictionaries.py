# Course: CIS 245 Introduction to Programming
# Instructor: Dr. Azizian
# Fall 2025
# Author: Joe Nowakowski
# Date Created: 10/29/2025

"""
Instructions: Create a program that includes a dictionary of stocks. 
Your dictionary should include at least 10 ticker symbols. 
The key should be the stock ticker symbol and the value should be the 
current price of the stock (the values can be fictional). Ask the user 
to enter a ticker symbol. Your program will search the dictionary for 
the ticker symbol and then print the ticker symbol and the stock price. 
If the ticker symbol is not located, print a message indicating that the 
ticker symbol was not found
"""

def main():
    """Main logic for program; gets stock ticker symbol and looks up price"""
    stocks = {
    "NVDA": 205.74,
    "AMZN": 231.12,
    "MSFT": 538.78,
    "AAPL": 268.78,
    "GOOG": 272.83,
    "TSM": 305.83,
    "AMD": 261.10,
    "META": 749.20,
    "INTC": 41.54,
    "GOLD": 4_011.00,
    }
    while True:
        ticker = get_stock_symbol()
        price = find_stock_price(ticker, stocks)

        if price is not None: # stock ticker was found in list of stocks and returned a price
            print(f"{ticker.upper()}'s stock price is ${price:,.2f}")
        else: # stock ticker was not found in list of stocks
            print(f"Sorry, {ticker.upper()} was not found")
        ans = input("Would you like to search another stock? [Y/N]: ").strip().lower()
        if ans not in ("y", "yes"): # if 'y' or 'yes', continues loop; otherwise ends program with 
            print("Goodbye!")       # a closing 'Goodbye!'
            break


def get_stock_symbol():
    """Gets stock symbol from user"""
    ticker = input("Please enter a ticker symbol for a stock, and if it's in" \
        "our records, the stock price will be displayed: ").strip()
    return ticker

def find_stock_price(ticker, stocks):
    """Finds ticker price in stocks. If ticker is not in stocks, returns None"""
    return stocks.get(ticker.upper())

if __name__ == "__main__":
    main()