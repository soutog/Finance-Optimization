from get_data import GetData

dataDir = "data/index_sample.csv"

data = GetData("01/12/2020", "05/07/2023")
data.import_data(dataDir)

# generate dataframe volatility
data.calculate_voltatility()
