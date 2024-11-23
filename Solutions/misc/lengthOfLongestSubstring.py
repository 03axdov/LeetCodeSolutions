def lengthOfLongestSubstring(s: str) -> int:
    maxLength = 0

    for t in range(len(s)):
        currentChars = []
        for char in s[t:]:
            
            if char not in currentChars:
                currentChars.append(char)
            else:
                break
            
        maxLength = max(maxLength, len(currentChars))
    
    return maxLength


print(lengthOfLongestSubstring(" "))