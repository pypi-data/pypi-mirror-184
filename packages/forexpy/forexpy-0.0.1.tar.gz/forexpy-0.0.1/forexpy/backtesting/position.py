from dataclasses import dataclass, field
from typing import Optional

from .forex_pip import Pip

@dataclass
class Position:
    """
    Holds the data for an open position
    
    Atributes:
        position_type(str): 'buy' or 'sell'
        entry_price (float): The price at which you open a position
        pair (str): The currency pair you wish to trade in, used to set pip size
        stop_loss_pips: Optional(Pip): Number of pips to set price at which you close to position to stop it from losing more
        take_profit_pips Optional(Pip): Number of pips to set price at which you wish to close to take the profits
    """
    
    position_type: str
    entry_price: float
    pair: str = "EURUSD"
    
    stop_loss_pips: Optional[Pip] = None
    take_profit_pips: Optional[Pip] = None
    
    pips: Pip = field(default=Pip, init=False)
    
    stop_loss: float = field(default=float, init=False)
    take_profit: float = field(default=float, init=False)
    
    def __post_init__(self):
        self.pips = Pip(0, self.pair)
        
        self.position_type = self.position_type.lower()
        
        if self.position_type == "buy":
            if self.stop_loss_pips:
                self.stop_loss = self.entry_price - (self.stop_loss_pips.amount * self.stop_loss_pips.pip_size)
                
            if self.take_profit:
                self.take_profit = self.entry_price + (self.take_profit_pips.amount * self.take_profit_pips.pip_size)
                

        if self.position_type == "sell":
            if self.stop_loss_pips:
                self.stop_loss = self.entry_price + (self.stop_loss_pips.amount * self.stop_loss_pips.pip_size)
                
            if self.take_profit:
                self.take_profit = self.entry_price - (self.take_profit_pips.amount * self.take_profit_pips.pip_size)