def isPalindrome(s):
    letters = "abcdefghijklmnopqrstuvwxyz0123456789"
    l, r = 0, len(s) - 1
    while l <= r:
        if s[l].lower() in letters and s[r].lower() in letters:
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
                continue
            else:
                return False
        else:
            if s[l].lower() not in letters:
                l += 1
            if s[r].lower() not in letters:
                r -= 1
    return True

print(isPalindrome(" "))