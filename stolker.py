import pandas as pd
import yfinance as yf
from os import path

def tracker(portfolio):
  tickers = {}

  for line in portfolio:
    temp = line.split()
    if len(temp) > 1:
      tickers[temp[0]] = temp[1:]

  ticker_names = list(tickers.keys())  

  data = yf.download(tickers = list(tickers.keys()), period='1d', interval='1m', group_by='ticker')
  data.dropna(inplace=True)

  total = 0.00
  total_pl = 0.00

  for ticker in ticker_names:
    cur_price = data[ticker].tail(1).iloc[0].Open
    if len(tickers[ticker]) > 0:
      owned = float(cur_price) * float(tickers[ticker][0])
      total += owned

      print(ticker + ": ${:.2f} @ ${:.2f}/share".format(owned, cur_price))


      if len(tickers[ticker]) > 1:
        sign = "+"
        avg_cost = float(tickers[ticker][0]) * float(tickers[ticker][1])
        cur_value = cur_price * float(tickers[ticker][0])
        pl = cur_value - avg_cost
        # TODO: pl_percent = 0.00

        total_pl += pl
        if pl < 0:
          sign = "-"
          pl *= -1

        print("\tP/L: " + sign + "$" + "{:.2f}".format(pl))
      print("\n")

  print("-----------------------------------")
  print("Total: \t\t$" + "{:.2f}".format(total))

  if total_pl < 0:
    sign = "-"
    total_pl *= -1
  else: 
    sign = "+"

  print("Total P/L: \t" + sign + "${:.2f}".format(total_pl)) 

if __name__ == "__main__":
  if path.exists("./portfolio.txt"):
    f = open("./portfolio.txt")
    r = f.read()
    l = r.split("\n")
    tracker(l)
  else:
    print("To begin, create a file in the project directory called `portfolio.txt`.")
    print("Use the following format on each line: <TICKER> <SHARES> <AVG COST [Optional]>")
