def isHappy(self, n):
    seen = set()

    current = n
    while current != 1 and current not in seen:
        seen.add(current)
        
        temp = 0
        for digit in str(current):
            temp += int(digit) ** 2
        current = temp
        
    return current not in seen