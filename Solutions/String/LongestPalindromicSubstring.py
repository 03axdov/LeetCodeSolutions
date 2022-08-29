def longestPalindrome(s):
    res = ""
    for i in range(len(s)):
        left, right = i - 1, i + 1
        
        while right < len(s) and s[right] == s[i]:
            right += 1
            
        while 0 <= left < right < len(s) and s[left] == s[right]:
            left, right = left - 1, right + 1
        
        if right - left - 1 > len(res):
            res = s[left+1:right]

    return res

print(longestPalindrome('cbbd'))


        