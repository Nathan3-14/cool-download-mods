from defaults.parent import Item

class Wood(Item):
    def __init__(self, start_stock: int):
        super().__init__("wood", 5.00, start_stock)

class Stone(Item):
    def __init__(self, start_stock: int):
        super().__init__("stone", 10.50, start_stock)

shop_items = [Wood, Stone]
