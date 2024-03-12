from defaults.parent import Block

class Wood(Block):
    def break_block(self):
        self.display_character = "~"
