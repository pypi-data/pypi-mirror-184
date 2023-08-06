import pandas as pd
import mplfinance as mpf

from .position import Position

class Grapher:
    """
    Plot candle-chart data and positions
    """
    
    def plot_candles(self, pair: str, df: pd.DataFrame(), positions: list[Position] = None):
        #To do: Add blankspace to the right, hline starts when position is opened
        hlines = []
        colours = []
        widths = []
        
        if positions:
            for position in positions:
                hlines.append(position.entry_price)
                colours.append("orange")
                widths.append(2)
                
                if position.stop_loss_pips:
                    hlines.append(position.stop_loss)
                    colours.append("red")
                    widths.append(5)
                    
                if position.take_profit_pips:
                    hlines.append(position.take_profit)
                    colours.append("green")
                    widths.append(5)
           
        mpf.plot(df,
                type='candle',
                style='charles',
                title=pair,
                ylabel='Price',
                hlines=dict(hlines=hlines ,colors=colours, linewidths=widths, alpha=0.6))