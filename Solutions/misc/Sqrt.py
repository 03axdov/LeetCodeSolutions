def mySqrt(x):
    previous = 0
    for i in range(x + 2):
        if i ** 2 > x:
            return previous
        previous = i

print(mySqrt(2147395599))