from defaults.parent import Item


class Pencil(Item):
    def __init__(self, start_stock: int):
        super().__init__("pencil", 5.00, start_stock)