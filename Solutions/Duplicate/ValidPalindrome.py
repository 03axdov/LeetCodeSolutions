def isPalindrome(s):
    letters = set("abcdefghijklmnopqrstuvwxyz1234567890")
    
    left = 0
    right = len(s) - 1

    while left < right:
        leftLetter = s[left].lower()
        rightLetter = s[right].lower()

        if leftLetter not in letters or rightLetter not in letters:
            if leftLetter not in letters: left += 1
            if rightLetter not in letters: right -= 1
        elif leftLetter == rightLetter:
            left += 1
            right -= 1
        else: break

    return left >= right


print(isPalindrome("A man, a plan, a canal: Panama"))