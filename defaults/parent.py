from typing import Tuple

class Item:
    def __init__(self, name: str, price: float, start_stock: int):
        self.name = name
        self.price = price
        self.stock = start_stock
    
    def buy(self, amount: int) -> Tuple[bool, float]:
        if self.stock >= amount:
            self.stock -= amount
            return (True, self.price * amount)
        else:
            return (False, 0)
    
    def __str__(self) -> str:
        return self.name