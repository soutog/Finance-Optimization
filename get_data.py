import datetime

# from tables import Column
import time

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd
import scipy.stats as stats
import yfinance as yf


def FormataStringData(data):
    dia = data.split("/")[0]
    mes = data.split("/")[1]
    ano = data.split("/")[2]

    return ano + "-" + mes + "-" + dia


class GetData:
    begin_date = ""
    end_date = ""
    dataDir = 0
    df = None

    def __init__(self, bdate, edate):
        self.begin_date = FormataStringData(bdate)
        self.end_date = FormataStringData(edate)

    def import_data(self, dataDir):
        self.dataDir = dataDir
        self.df = pd.read_csv(dataDir, sep=";")

        start = time.time()

        df_stock = pd.DataFrame()
        stock_list = self.df["Ticker"].tolist()
        # stock_list.append('IVVB11.SA')
        stock_list.append("^GSPC")
        for stock in stock_list:
            df_stock[stock] = yf.download(
                stock, start=self.begin_date, end=self.end_date
            )["Adj Close"]

        # df_stock=df_stock.fillna(method="bfill")

        # Stocks removed if data of the stock is not complete
        df_stock = df_stock.dropna(axis=1)

        end = time.time()
        print("Elapsed Time Seq: " + str(end - start))

        returns_stocks = df_stock.pct_change()
        returns_stocks = returns_stocks[1:]
        returns_stocks_acm = (1 + returns_stocks).cumprod()

        print(returns_stocks_acm)

        returns_stocks_acm.to_csv("./data/stocks_s&p.csv")


dataDir = "./data/index_sample.csv"
GetData("01/01/2009", "31/12/2019").import_data(dataDir)
