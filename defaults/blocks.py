from .parent import Block


class CoolBlock(Block):
    def break_block(self):
        return super().break_block(":D")