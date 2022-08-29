def findAnagrams(s, p):
    output = []
    for t in range(len(s)):
        if t + len(p) <= len(s):
            if sorted(s[t:t+len(p)]) == sorted(p):
                output.append(t)
        else:
            break
    
    return output


print(findAnagrams("abab", "ab"))