def myAtoi(s):
    digits = "1234567890"
    result = '0'
    positive = 1
    plus_minus_valid = True
    for t, char in enumerate(s):
        if char == ' ' and plus_minus_valid:
            continue
        elif char == '-' and plus_minus_valid:
            positive = -1
            plus_minus_valid = False
        elif char == '+' and plus_minus_valid:
            positive = 1
            plus_minus_valid = False
        elif char in digits:
            result += char
            plus_minus_valid = False
            if t != len(s) - 1:
                if s[t+1] not in digits:
                    break
        elif char not in digits:
            break
    if -2**31 <= int(result) * positive <= 2**31 - 1:
        return int(result) * positive
    elif -2**31 > int(result) * positive:
        return -2**31
    elif 2**31 - 1 < int(result) * positive:
        return 2**31 - 1


print(myAtoi("2147483647"))