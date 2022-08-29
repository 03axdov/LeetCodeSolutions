def isPalindrome(x):
    l, r = 0, len(str(x)) - 1
    while l <= r:
        if str(x)[l] == str(x)[r]:
            l += 1
            r -= 1
        else:
            return False
    return True


print(isPalindrome(10))