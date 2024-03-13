from defaults.parent import Item


class A(Item):
    def __init__(self, start_stock: int):
        super().__init__("A", 0.1, start_stock)

class B(Item):
    def __init__(self, start_stock: int):
        super().__init__("B", 0.5, start_stock)