from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Pip:
    """
    Holds pip data
    
    Atributes:
        amount (int): Number of pips
        pair (str): The currency pair you wish to trade in, used to set pip size
    """
    
    amount: int
    pair: Optional[str] = "EURUSD"
    
    pip_size: float = field(default=float, init=False)
    pair_pip_sizes: dict = field(default_factory=dict, init=False)
    
    def __post_init__(self):
        self.pair_pip_sizes = {"EURUSD": 0.0001}
        self.pip_size = self.pair_pip_sizes[self.pair]