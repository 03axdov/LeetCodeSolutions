def longestPalindrome(s: str) -> str:

    windowSize = len(s)
    
    while windowSize > 1:
        for start in range(len(s) - windowSize + 1):
            substring = s[start:start+windowSize]
            if substring == substring[::-1]:
                return substring
        windowSize -= 1

    return s[0]