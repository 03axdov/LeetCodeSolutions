def concatenatedBinary(n: int) -> int:
    current = ""
    for i in range(1, n + 1):
        current += str(bin(i)[2:])

    return int(current, 2) % (10**9 + 7)


print(concatenatedBinary(8259))