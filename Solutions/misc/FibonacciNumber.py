def fib(n: int) -> int:
    nums = {0: 0, 1: 1, 2: 1, 3: 2}
    if n not in nums.keys():
        return fib(n-1) + fib(n-2)
    else:
        return nums[n]


print(fib(5))