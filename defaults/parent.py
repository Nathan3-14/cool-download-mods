class Block:
    def __init__(self, icon: str) -> None:
        self.display_icon = icon
        self.position = [0, 0]
    
    def __str__(self) -> str:
        return self.display_icon

    def tick(self) -> None:
        pass

