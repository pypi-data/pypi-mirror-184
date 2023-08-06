from dataclasses import dataclass, field

from .position_manager import Position_manager
from .data_manager import Data_manager
from .forex_pip import Pip

@dataclass
class Backtester:
    """
    Backtest on Forex historical data
    """
    
    position_balances: list[float] = field(default_factory=list[float], init=False)
    
    position_manager: Position_manager = field(default=Position_manager(), init=False)
    data_manager: Data_manager = field(default=Data_manager(), init=False)   
    
    def open_position(self, position_type: str, pair: str, stop_loss_pips: int = None, take_profit_pips: int = None):
        if stop_loss_pips:
            stop_loss_pips = Pip(amount=stop_loss_pips, pair=pair)
        
        if take_profit_pips:
            take_profit_pips = Pip(amount=take_profit_pips, pair=pair)
        
        self.position_manager.open_positon(position_type=position_type,
                                           entry_price=self.data_manager.current_candles[pair][1]["Open"],
                                           pair=pair,
                                           stop_loss_pips=stop_loss_pips,
                                           take_profit_pips=take_profit_pips)
        
    
    def close_position(self, position_index: int):
        self.position_balances.append(self.position_manager.positions[position_index].pips.amount)
        self.position_manager.close_position(position_index=position_index)
    
    def update_positions(self):
        self.position_manager.update_positions(current_prices=self.data_manager.current_candles)
      
    def check_positions(self):
        for i, position in enumerate(self.position_manager.positions):
            
            if position.position_type == "buy":
                if position.stop_loss_pips:
                    if self.data_manager.current_candles[position.pair][1]["Low"] < position.stop_loss:
                        print(f"Closed position {i} (SL): {position.pips.amount} pips")
                        self.close_position(position_index=i)
                        
                    
                if position.take_profit_pips:
                    if self.data_manager.current_candles[position.pair][1]["High"] > position.take_profit:
                        print(f"Closed position {i} (TP): {position.pips.amount} pips")
                        self.close_position(position_index=i)
                    
                        
            elif position.position_type == "sell":
                if position.stop_loss_pips:
                    if self.data_manager.current_candles[position.pair][1]["High"] > position.stop_loss:
                        print(f"Closed position {i} (SL): {position.pips.amount} pips")
                        self.close_position(position_index=i)
                        
                    
                if position.take_profit_pips:
                    if self.data_manager.current_candles[position.pair][1]["Low"] < position.take_profit:
                        print(f"Closed position {i} (TP): {position.pips.amount} pips")
                        self.close_position(position_index=i)
                        
    def update(self, graph: bool = False):
        if graph:
            self.data_manager.show_data(open_positions=self.position_manager.positions)
        
        self.update_positions()
        self.check_positions()
        self.data_manager.next_candles()   
    
    
