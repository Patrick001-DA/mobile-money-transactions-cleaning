# Mobile Money Transactions: Data Cleaning & Analysis (Python)

A pandas/NumPy project that cleans and analyses a synthetic dataset of 300 mobile money transactions (Send, Withdraw, Deposit, Paybill, Airtime) across five Kenyan counties. The data is deliberately dirty to practise real-world cleaning.

## What the script does
- Inspects the data with `info()`, `head()`, `isna().sum()` and `shape`
- Removes duplicate transactions (by `txn_id`)
- Standardises the `type` column (strip spaces, title case)
- Fills missing `amount` with the median for that transaction type, and missing `county` with "Unknown"
- Converts `date` to datetime and creates a `month` column
- Aggregates total, average and count by transaction type
- Builds a pivot table of total amount by month and type
- Finds the top 3 counties by transaction count
- Flags large transactions (> KES 15,000) and calculates their share of total value

## Tools
Python, pandas, NumPy

## How to run
pip install pandas numpy
python mobile_money_transactions.py

## Key findings
(Add 3 to 4 bullets after running: top transaction type by value, top 3 counties, % of value from large transactions.)
