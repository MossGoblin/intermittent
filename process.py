from tree import *

def process_string(string: str):

    # 1. cleanup
    # string = string.replace(' ', '')

    # 2. split
    chunks = string.split()

    operators = ['+', '-', '*', '-']
    operands = []

    for chunk in chunks:
        if chunk in operators:
            # split tree
            pass
        else:
            operand = int(chunk)
            operands.append(Tree(operand))
        # HERE - find out what the ordering should be
    pass
