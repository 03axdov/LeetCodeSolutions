def reverse(x):
    is_negative = False
    if str(x)[0] == '-':
        is_negative = True
        x = -x
    if -2**31 <= int(str(x)[::-1]) <= 2**31 - 1:
        if is_negative:
            return int('-' + str(x)[::-1])
        else:
            return int(str(x)[::-1])
    return 0

print(reverse(2147483641))