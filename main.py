from get_data import GetData
import pandas as pd

dataDir = "data/index_sample.csv"

data = GetData("01/12/2021", "05/07/2023")
data.import_data(dataDir)


stock_data = "data/stocks_indicators.csv"


# generate dataframe volatility
data.calculate_volatility(stock_data)

# df = pd.read_csv('data/stocks_s&p_test.csv')
# print(df.head())