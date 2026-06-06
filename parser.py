import csv
from typing import Iterator
from trade import Trade

class Parser:
    def load_trades(self, file_name: str) -> Iterator[Trade]:
        with open(file_name, newline="") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                yield self.parse_trade(row)

    def parse_trade(self, row: list[str]) -> Trade:
        if len(row) != 4:
            raise ValueError("row does not have 4 fields")

        symbol, side, quantity, price = row

        symbol = symbol.strip().upper()
        side = side.strip().upper()
        quantity = quantity.strip()
        price = price.strip()

        if symbol == "":
            raise ValueError("symbol is empty")

        if side not in ("BUY", "SELL"):
            raise ValueError("side is not BUY or SELL")

        try:
            quantity = int(quantity)
        except ValueError as exc:
            raise ValueError("quantity must be an integer") from exc

        try:
            price = float(price)
        except ValueError as exc:
            raise ValueError("price must be a number") from exc

        if quantity <= 0:
            raise ValueError("quantity must be greater than 0")

        if price <= 0:
            raise ValueError("price must be greater than 0")

        trade = Trade(symbol, side, quantity, price)
        return trade






