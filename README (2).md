# Stock Portfolio Tracker

A simple command-line Python program that calculates the total value of a stock portfolio using manually defined (hardcoded) stock prices.

## Features

- Enter stock names and quantities interactively
- Prices come from a hardcoded dictionary
- Input validation for unknown stocks and invalid quantities
- Displays a formatted table with the total investment value
- Optionally saves the result to a `.txt` or `.csv` file

## Concepts Used

Dictionary, input/output, basic arithmetic, file handling

## Requirements

- Python 3.6 or higher
- No external libraries needed (uses only the built-in `csv` module)

## How to Run

```bash
python stock_portfolio_tracker.py
```

## Stock Prices

Defined in the `STOCK_PRICES` dictionary at the top of the script:

| Stock | Price (USD) |
|-------|-------------|
| AAPL  | 180 |
| TSLA  | 250 |
| GOOGL | 140 |
| MSFT  | 330 |
| AMZN  | 125 |

Edit the dictionary to add or change stocks.

## Usage

1. Type a stock name (e.g. `AAPL`), then the quantity.
2. Repeat for each stock. Type `done` when finished.
3. View the summary table and total investment.
4. Choose `txt`, `csv`, or `no` to save the result.

## Sample Output

```
Stock name: aapl
Quantity of AAPL: 10
  Added 10 x AAPL @ $180 = $1800

Stock name: tsla
Quantity of TSLA: 5
  Added 5 x TSLA @ $250 = $1250

Stock name: msft
Quantity of MSFT: 2
  Added 2 x MSFT @ $330 = $660

Stock name: done

==============================================
Stock        Qty     Price         Value
----------------------------------------------
AAPL          10       180          1800
TSLA           5       250          1250
MSFT           2       330           660
----------------------------------------------
Total Investment:                        $3710
==============================================

Save result to file? (txt / csv / no): csv
Saved to portfolio.csv
```

## Project Structure

```
.
├── stock_portfolio_tracker.py
├── sample_output.txt
├── README.md
└── .gitignore
```
