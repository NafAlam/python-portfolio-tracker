from trade import Trade
from collections import defaultdict

class Portfolio:
    def __init__(self):
        self.trades = []

    def add_trade(self, trade: Trade) -> None:
        self.trades.append(trade)

    def calculate_position(self) -> defaultdict[str, int]:
        position = defaultdict(int)
        for trade in self.trades:
            if trade.side == "BUY":
                position[trade.symbol] += trade.quantity
            else:
                position[trade.symbol] -= trade.quantity

        return position

    def average_entry_price(self) -> defaultdict[str, float]:
        trade_shares_bought = defaultdict(int)
        trade_total_cost = defaultdict(int)

        for trade in self.trades:
            if trade.side == "BUY":
                trade_shares_bought[trade.symbol] += trade.quantity
                trade_total_cost[trade.symbol] += (trade.quantity * trade.price)

        avg_entry_price = defaultdict(float)
        for symbol in trade_shares_bought:
            total_cost = trade_total_cost[symbol]
            shares_bought = trade_shares_bought[symbol]
            avg_entry_price[symbol] = total_cost / shares_bought

        return avg_entry_price






