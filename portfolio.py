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



