from defaults.parent import Block


class A(Block):
    def __init__(self):
        super().__init__("A")
    
    def tick(self) -> None:
        self.position[0] += 1

class B(Block):
    def __init__(self):
        super().__init__("B")
        self.position[0] -= 1

class Empty:
    def __str__(self) -> str:
        return " "
