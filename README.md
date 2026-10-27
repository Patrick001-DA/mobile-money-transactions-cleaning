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
- **Data quality:** The raw data had 308 rows, 17 missing amounts and 10 missing counties. After removing 8 duplicate transactions (by `txn_id`) and standardising the `type` column, the dataset had 300 clean rows.
- **Top transaction type by value:** Airtime led with KES 825,887 across 74 transactions (average KES 11,161), followed by Deposit at KES 738,771. Together they account for about 51% of total value.
- **Top 3 counties by volume:** Nakuru (65), Mombasa (60) and Kisumu (56).
- **Large transactions:** Transactions above KES 15,000 make up 42.0% of total value.
- **Monthly trend:** April looks like a sharp drop, but the data only covers about 100 days (1 Jan to around 10 Apr), so April is a partial month and not a real decline.
- **Note:** The dataset is synthetic and randomly generated, so these figures illustrate the method, not real mobile money behaviour.
