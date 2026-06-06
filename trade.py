class Trade:
    def __init__(self, symbol: str, side: str, quantity: int, price: float):
        self.symbol = symbol
        self.side = side
        self.quantity = quantity
        self.price = price

    def __repr__(self):
        return f"Trade(symbol={self.symbol!r}, side={self.side!r}, quantity={self.quantity}, price={self.price})"

