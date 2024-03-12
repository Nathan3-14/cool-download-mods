class Block:
    def __init__(self, name: str, character: str):
        self.name = name
        self.display_character = character
    
    def __str__(self) -> str:
        return f"{self.display_character}"