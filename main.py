import sys
from portfolio import Portfolio
from parser import Parser

def main() -> None:
    portfolio = Portfolio()
    parser = Parser()


    try:
        for trade in parser.load_trades("trades.csv"):
            portfolio.add_trade(trade)
    except ValueError as error:
        print(f"Could not load trades: {error}")
        sys.exit(1)

    positions = portfolio.calculate_position()
    print("Positions")
    for symbol, quantity in positions.items():
        print(f"{symbol}: {quantity} shares")

    print()

    avg_entry_price = portfolio.average_entry_price()
    print("Average Entry Prices")
    for symbol, price in avg_entry_price.items():
        print(f"{symbol}: £{price:.2f}")

    print()

    total_pnl = portfolio.realized_pnl()
    print("Realized PnL")
    print(f"£{total_pnl:.2f}")

if __name__ == "__main__":
    main()
