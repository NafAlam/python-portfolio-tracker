from portfolio_tracker.portfolio import Portfolio
from portfolio_tracker.trade import Trade


def make_portfolio(trades: list[Trade]) -> Portfolio:
    portfolio = Portfolio()

    for trade in trades:
        portfolio.add_trade(trade)

    return portfolio


def test_calculate_position():
    portfolio = make_portfolio(
        [
            Trade("AAPL", "BUY", 10, 100.0),
            Trade("AAPL", "SELL", 5, 110.0),
            Trade("MSFT", "BUY", 3, 300.0),
        ]
    )

    assert dict(portfolio.calculate_position()) == {
        "AAPL": 5,
        "MSFT": 3,
    }


def test_average_entry_price_uses_only_buy_trades():
    portfolio = make_portfolio(
        [
            Trade("AAPL", "BUY", 10, 100.0),
            Trade("AAPL", "SELL", 5, 110.0),
            Trade("MSFT", "BUY", 3, 300.0),
        ]
    )

    assert dict(portfolio.average_entry_price()) == {
        "AAPL": 100.0,
        "MSFT": 300.0,
    }


def test_average_entry_price_with_multiple_buys():
    portfolio = make_portfolio(
        [
            Trade("AAPL", "BUY", 10, 100.0),
            Trade("AAPL", "BUY", 5, 120.0),
        ]
    )

    assert portfolio.average_entry_price()["AAPL"] == 1600 / 15


def test_realized_pnl():
    portfolio = make_portfolio(
        [
            Trade("AAPL", "BUY", 10, 100.0),
            Trade("AAPL", "SELL", 5, 110.0),
            Trade("MSFT", "BUY", 3, 300.0),
        ]
    )

    assert portfolio.realized_pnl() == 50.0
