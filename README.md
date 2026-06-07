# Python Portfolio Tracker

A small Python command-line app for tracking stock trades from a CSV file.

The app currently:

- reads trades from `trades.csv`
- sanitizes and validates trade rows
- calculates current positions
- calculates average entry prices
- calculates realized PnL

## Project Structure

```text
python-portfolio-tracker/
├── portfolio_tracker/
│   ├── __init__.py
│   ├── main.py
│   ├── parser.py
│   ├── portfolio.py
│   └── trade.py
├── tests/
│   ├── test_parser.py
│   └── test_portfolio.py
├── trades.csv
└── README.md
```

## CSV Format

Each row in `trades.csv` should use this format:

```text
symbol,side,quantity,price
```

Example:

```text
AAPL,BUY,10,100
AAPL,SELL,5,110
MSFT,BUY,3,300
```

Valid sides are:

- `BUY`
- `SELL`

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install test dependencies:

```bash
python -m pip install pytest
```

## Run The App

From the project root:

```bash
python -m portfolio_tracker.main
```

Expected output for the sample `trades.csv`:

```text
Positions
AAPL: 5 shares
MSFT: 3 shares

Average Entry Prices
AAPL: £100.00
MSFT: £300.00

Realized PnL
£50.00
```

## Run Tests

From the project root:

```bash
python -m pytest
```

If your shell is not using the virtual environment, run:

```bash
.venv/bin/python -m pytest
```
