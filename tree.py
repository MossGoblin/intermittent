from typing import Union, Type

class Tree:

    def __init__(self, state = None):
        self.state: Union[Type, (Type, (Tree, Tree))] = state