from dataclasses import dataclass, field

import pandas as pd

from .position import Position
from .forex_pip import Pip

@dataclass
class Position_manager:
    """
    Manages positions
    
    Opens, closes and updates positions
    """
    
    positions: list[Position] = field(init=False, default_factory=list[Position])
    
    def open_positon(self, position_type: str, entry_price: float, pair: str, stop_loss_pips: Pip = None, take_profit_pips: Pip = None):
        
        """
        Opens a position
        
        Atributes:
            position_type(str): 'buy' or 'sell'
            entry_price (float): The price at which you open a position
            pair (str): The currency pair you wish to trade in, used to set pip size
            stop_loss_pips: Optional(Pip): Number of pips to set price at which you close to position to stop it from losing more
            take_profit_pips Optional(Pip): Number of pips to set price at which you wish to close to take the profits
        """
        
        new_position = Position(position_type=position_type, entry_price=entry_price, pair=pair, stop_loss_pips=stop_loss_pips, take_profit_pips=take_profit_pips)
        self.positions.append(new_position)
        
    def close_position(self, position_index: int):
        """
        Closes a position
        
        Atributes:
            position_index (int): The index of the position you wish to close
        """
        
        self.positions.remove(self.positions[position_index])
        
    def update_positions(self, current_prices: dict[str, list[int, pd.Series(object)]]):
        """
        Updates all open positione
        
        Atributes:
            current_price (dict): Dictionary contary key-value pairs consisting of: pair(str): pair current price(float)
        """
        
        for position in self.positions:
            if position.position_type == "buy":
                position.pips.amount = round(current_prices[position.pair][1]["Close"] - position.entry_price, 5) / position.pips.pip_size
                 
            elif position.position_type == "sell":
                position.pips.amount = round(position.entry_price - current_prices[position.pair][1]["Close"], 5) / position.pips.pip_size