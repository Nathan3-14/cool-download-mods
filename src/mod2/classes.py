class Fruit:
    def __init__(self, name: str):
        self.name = name

    def eat(self, amount: int = 1):
        print(f"You are eating {amount} {self.name}")
