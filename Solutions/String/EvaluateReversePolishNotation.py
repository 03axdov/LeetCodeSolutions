from typing import List
import math

def evalRPN(tokens: List[str]) -> int:
    operators = {"+" : lambda l: l[0] + l[1],
                 "-": lambda l: l[0] - l[1],
                 "/": lambda l: int(l[0] / l[1]),
                 "*": lambda l: l[0] * l[1]}
    
    idx = 0
    while idx < len(tokens):
        token = tokens[idx]
        if token in operators.keys():
            tokens[idx-2] = operators[token]([int(tokens[idx-2]), int(tokens[idx-1])])
            tokens.pop(idx)
            tokens.pop(idx-1)
            idx -= 2
        else:
            tokens[idx] = int(tokens[idx])
        idx += 1

    return sum(tokens)

print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))