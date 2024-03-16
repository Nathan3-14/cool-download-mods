from defaults.parent import Block


class A(Block):
    def __init__(self) -> None:
        super().__init__("A")
    
    def tick(self) -> None:
        self.position[0] += 1

class B(Block):
    def __init__(self):
        super().__init__("B")
    
    def tick(self) -> None:
        self.position[0] -= 1

class Empty(Block):
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        return " "
