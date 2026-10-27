import numpy as np
import pandas as pd
rng = np.random.default_rng(7)
n = 300
df = pd.DataFrame({
 "txn_id": np.arange(1, n + 1),
 "date": pd.date_range("2026-01-01", periods=n, freq="8h").strftime("%Y-%m-%d"),
 "type": rng.choice(["Send", "Withdraw", "Deposit", "Paybill", "Airtime"], n),
 "amount": rng.integers(50, 20000, n).astype(float),
 "county": rng.choice(["Nairobi", "Kajiado", "Mombasa", "Kisumu", "Nakuru"], n),
})
# make the data dirty on purpose
df.loc[rng.choice(n, 15, replace=False), "amount"] = np.nan
df.loc[rng.choice(n, 10, replace=False), "county"] = np.nan
df = pd.concat([df, df.sample(8, random_state=1)], ignore_index=True) # duplicates
df.loc[::7, "type"] = df.loc[::7, "type"].str.upper()
df.loc[::11, "type"] = df.loc[::11, "type"] + " "
#Use info(), head() and isna().sum() to inspect the data. How many rows, and how many missing values per column?
print(df.info())
print(df.head().to_string())
print(df.isna().sum())
print(df.shape)
#There are 308 rows.
# amount and county  has 17 and 10 missing values respectively.

#Remove duplicate rows (duplicates share the same txn_id). How many were removed?
print(df.duplicated().sum())
df=df.drop_duplicates(subset="txn_id")
print(df.duplicated().sum())


#Clean the type column: strip spaces and use title case. Confirm there are exactly 5 unique values.
df["type"]=df["type"].str.strip().str.title()
print(df["type"].nunique(),df["type"].unique())

#Fill missing amount with the median amount of that transaction type. Fill missing county with 'Unknown

df["amount"]=df["amount"].fillna(df.groupby("type")["amount"].transform("median"))

df["county"]=df["county"].fillna("Unknown")
print(df.isna().sum())

#Convert date to datetime and create a month column (e.g. 2026-01).
df["date"]=pd.to_datetime(df["date"],errors="coerce")
df["month"] = df["date"].dt.strftime("%Y-%m")



#Total, average and count of amount by type, sorted by total (largest first).
print(df.groupby("type")["amount"].agg(total="sum", average="mean",count="count").sort_values("total", ascending= False).round(0))



#Create a pivot table: rows = month, columns = type, values = total amount.
pivot=df.pivot_table(index="month",columns="type",values="amount",aggfunc="sum")

print(pivot.round(0))



#Which 3 counties have the most transactions?

highest_transactions=df["county"].value_counts().head(3)

print(highest_transactions)






#Flag large transactions (amount above 15,000). What percentage of the total value do they make up?

df["is_large"] = df["amount"] > 15000
pct = df.loc[df["is_large"], "amount"].sum() / df["amount"].sum() * 100
print(f"Large transactions make up {pct:.1f}% of total value")










