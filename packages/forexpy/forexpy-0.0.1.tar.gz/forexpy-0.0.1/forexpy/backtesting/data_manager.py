from dataclasses import dataclass, field

import pandas as pd

from .grapher import Grapher
from .position import Position

@dataclass
class Data_manager:
    
    """
    Manages forex historic data
    
    Works with OHLC .csv file
    """
    
    datasets: dict = field(default_factory=dict[str, pd.DataFrame()], init=False)
    current_candles: dict = field(default_factory=dict[str, list[int, pd.Series(object)]], init=False)
    
    grapher: Grapher = field(default=Grapher(), init=False)
    
    def load_data(self, pair: str, path: str, nrows: int = 10):
        """
        Loads historic data
        
        File is an OHLC .csv file with dates, loads file into self.datasets
        
        Attributes:
            pair (str): The pair from which the file's data comes from
            path (str): The path to an OHLC .csv file
        """
        
        df = pd.read_csv(path, parse_dates=True, index_col=0, nrows=nrows)
        
        self.datasets[pair] = df

        self.current_candles[pair] = [0, self.datasets[pair].iloc[0]]
    
    def next_candles(self):
        """
        Moves to the next candle
        
        Next row in dataframe
        """
        
        for pair, candle_data in self.current_candles.items():
            self.current_candles[pair] = [(candle_data[0] + 1), self.datasets[pair].iloc[(candle_data[0] + 1)]]
            
    def show_data(self, open_positions: list[Position] = None):
        print("Plotted")
        for df_data, current_candle_data, in zip(self.datasets.items(), self.current_candles.values()):
            if open_positions:
                self.grapher.plot_candles(pair=df_data[0][:current_candle_data[0]], df=df_data[1], positions=open_positions)
            else:
                self.grapher.plot_candles(pair=df_data[0][:current_candle_data[0]], df=df_data[1])