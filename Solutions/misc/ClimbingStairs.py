def climbStairs(n):
    steps = {1: 1, 2: 2, 3: 3}
    current = 4
    while n not in steps.keys():
        steps[current] = steps[current-1] + steps[current-2]
        current += 1

    return steps[n]

print(climbStairs(3))

# 2: 2
# 3: 3
# 4: 5
# 5: 8