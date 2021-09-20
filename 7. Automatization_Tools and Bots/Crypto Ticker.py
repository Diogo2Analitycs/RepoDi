#imports
import pandas as pd
from binance.client import Client
import time


api_key = "insert ur api key from binance"
api_secret = "insert ur api key from binance"
client = Client(api_key, api_secret)

#Price for all selected coins

Coins = ["BTCEUR","BTCUSD","ETHEUR","XRPEUR","DOGEEUR","SNGLSBTC","RVNUSD"]

All_Tickets = pd.DataFrame.from_dict(client.get_all_tickers())

All_Tickets.loc[(All_Tickets["symbol"] == "BTCEUR") | (All_Tickets["symbol"] == "BTCUSD") | 
                (All_Tickets["symbol"] == "ETHEUR") | (All_Tickets["symbol"] == "XRPEUR") |
                (All_Tickets["symbol"] == "DOGEEUR") | (All_Tickets["symbol"] == "SNGLSBTC") |
                (All_Tickets["symbol"] == "RVNUSD")]

time.sleep(15)
