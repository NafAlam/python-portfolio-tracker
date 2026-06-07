from portfolio_tracker.parser import Parser
from portfolio_tracker.trade import Trade
import pytest

parser = Parser()


def test_parse_trade_returns_trade():
    trade = parser.parse_trade(["AAPL", "BUY", "10", "100"])

    assert trade == Trade("AAPL", "BUY", 10, 100.0)


def test_parse_trade_sanitizes_symbol_and_side():
    trade = parser.parse_trade(["  aapl ", "   bUy ", " 10 ", " 100 "])

    assert trade == Trade("AAPL", "BUY", 10, 100.0)


def test_parse_trade_rejects_invalid_side():
    with pytest.raises(ValueError, match="side is not BUY or SELL"):
        parser.parse_trade(["AAPL", "HOLD", "10", "100"])


def test_parse_trade_rejects_invalid_quantity():
    with pytest.raises(ValueError, match="quantity must be an integer"):
        parser.parse_trade(["AAPL", "BUY", "abc", "100"])


def test_parse_trade_rejects_empty_symbol():
    with pytest.raises(ValueError, match="symbol is empty"):
        parser.parse_trade([" ", "BUY", "10", "100"])


def test_parse_trade_rejects_zero_quantity():
    with pytest.raises(ValueError, match="quantity must be greater than 0"):
        parser.parse_trade(["AAPL", "BUY", "0", "100"])


def test_parse_trade_rejects_negative_quantity():
    with pytest.raises(ValueError, match="quantity must be greater than 0"):
        parser.parse_trade(["AAPL", "BUY", "-1", "100"])


def test_parse_trade_rejects_invalid_price():
    with pytest.raises(ValueError, match="price must be a number"):
        parser.parse_trade(["AAPL", "BUY", "10", "abc"])


def test_parse_trade_rejects_zero_price():
    with pytest.raises(ValueError, match="price must be greater than 0"):
        parser.parse_trade(["AAPL", "BUY", "10", "0"])


def test_parse_trade_rejects_negative_price():
    with pytest.raises(ValueError, match="price must be greater than 0"):
        parser.parse_trade(["AAPL", "BUY", "10", "-1"])


def test_parse_trade_rejects_wrong_number_of_fields():
    with pytest.raises(ValueError, match="row does not have 4 fields"):
        parser.parse_trade(["AAPL", "BUY", "10"])
