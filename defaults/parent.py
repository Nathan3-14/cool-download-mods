class Block:
    def __init__(self, name: str, character: str):
        self.name = name
        self.display_character = character
    
    def break_block(self, break_char: str): #! Required in subclasses
        self.display_character = break_char

    def __str__(self) -> str:
        return f"{self.display_character}"