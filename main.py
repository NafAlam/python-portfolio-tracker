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
print(positions)

avg_entry_price = portfolio.average_entry_price()
print(avg_entry_price)

total_pnl = portfolio.realized_pnl()
print(total_pnl)
