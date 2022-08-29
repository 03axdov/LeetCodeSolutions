combinations = {1: 1, 2: 2, 3: 3}
def climbStairs(n: int) -> int:
    if n not in combinations.keys():
        combinations[n] = climbStairs(n-1) + climbStairs(n-2)
    return combinations[n]


print(climbStairs(45))