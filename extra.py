import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class TickerApp:
    def __init__(self):
        self.ticker = input("Enter ticker: ")
    def getTicker(self):
        self.tickerSymbol = yf.Ticker(self.ticker)
        self.tickerClose = self.tickerSymbol.history(period='max')['Close']
    def plotSymbol(self):
        self.tickerClose.plot()
        plt.show()
    def otherCrap(self):
        # build a rectangle in axes coords
        left, width = .05, .8
        bottom, height = .05, .8
        right = left + width
        top = bottom + height

        fig = plt.figure()
        ax = fig.add_axes([0, 0, 1, 1])
      
        arg = self.tickerSymbol.info['longBusinessSummary']

        ax.text(0.5*(left+right), 0.5*(bottom+top), f'{str(arg)}',
                horizontalalignment='center',
                verticalalignment='center',
                fontsize=12, color='black',
                wrap=True,
                transform=ax.transAxes)

        ax.set_axis_off()
        plt.show()


def main():
    app = TickerApp()
    app.getTicker()
    app.plotSymbol()
    app.otherCrap()

main()




