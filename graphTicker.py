import matplotlib.pyplot as plt
import yfinance as yf


def graphTicker(ticker):
    '''Plot ticker'''
    tickerTitle = ticker
    ticker = yf.Ticker(ticker)
    tickerClose = [i for i in ticker.history(period='max')['Close']]
    plt.title(tickerTitle)
    plt.plot(tickerClose)
    plt.show()


while True:
    graphTicker(input('Enter Ticker symbol: \n'))

