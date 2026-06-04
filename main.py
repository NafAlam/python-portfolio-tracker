import csv
from trade import Trade
from portfolio import Portfolio

portfolio = Portfolio()

with open('trades.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        symbol, side, quantity, price = row
        trade = Trade(symbol, side, int(quantity), int(price))
        portfolio.add_trade(trade)

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
