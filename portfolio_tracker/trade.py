from dataclasses import dataclass


@dataclass(frozen=True)
class Trade:
    symbol: str
    side: str
    quantity: int
    price: float

