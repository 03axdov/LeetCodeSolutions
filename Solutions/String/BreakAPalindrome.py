def breakPalindrome(palindrome: str) -> str:
    if len(palindrome) <= 1: return ""

    letters = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    finished = False
    
    for t, char in enumerate(palindrome):
        if char != 'a' and not finished and t != len(palindrome) // 2:
            idx = letters.index(char)
            char = "a"
            finished = True

        result += char

    if result == palindrome:    # Only a:s
        return result[:-1] + "b"

    return result


print(breakPalindrome("aba"))