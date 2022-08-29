numbers = {0: 0, 1: 1, 2: 1}
def tribonacci(n: int) -> int:
    global numbers 
    if n not in numbers.keys():
        numbers[n] = tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)
    return numbers[n]


print(tribonacci(25))