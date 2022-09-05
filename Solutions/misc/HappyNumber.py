from collections import Counter
def isHappy(n: int):
    count = Counter()
    current = n

    while True:
        if current == 1: return True
        if count[current] != 0: return False

        new = 0
        for char in str(current):
            new += int(char) ** 2

        count[current] += 1
        current = new
        

print(isHappy(2))