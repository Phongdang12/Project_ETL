"""
Python Extract Transform Load Example
"""
import pymysql
import sqlalchemy
import requests
import json
import pandas as pd
# Extract data from Alpha Vantage API
API_URL = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&outputsize=full&apikey=demo"
data = requests.get(API_URL).json()
json_str = json.dumps(data, indent=4)

# Transform data into a pandas DataFrame
time_series = data.get("Time Series (5min)", {})

df = pd.DataFrame.from_dict(time_series, orient='index')

df = df.dropna()
df = df.rename(columns=lambda x: x.split('. ')[1])  

for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

df['date']=pd.to_datetime(df.index).date
df['time']=pd.to_datetime(df.index).time

df.reset_index(inplace=True)
df.reset_index(drop=True, inplace=True) 
df.drop(df.columns[0], axis=1, inplace=True)  

# Load data into MySQL database
username = 'root'
password = 'doanhbietemnghigi'
host = 'localhost'
database = 'test'

engine = sqlalchemy.create_engine(
    f"mysql+pymysql://{username}:{password}@{host}/{database}"
)


table_name = 'stock_price'  
df.to_sql(
    name=table_name,
    con=engine,
    index=False,
    if_exists='replace'  
)

print("Saved to MySQL!")
print(df.head())
