from defaults.parent import Block

class Stone(Block):
    def break_block(self):
        self.display_character = " "
