import itertools

def generateParenthesis(n):
    parenthesis = []
    for _ in range(n):
        parenthesis.append('(')
        parenthesis.append(')')
    print(parenthesis)
    permutations = []
    for permutation in itertools.permutations(parenthesis, 2*n):
        permutations.append(permutation)
    print(permutation)

generateParenthesis(3)