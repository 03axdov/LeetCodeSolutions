def findSubstring(s, words):
    output = []
    current = []
    length = len(words[0])
    for start_idx in range(len(s)):
        if start_idx > len(s) - len(words) * length + 1:
            break
        if s[start_idx:start_idx+length] in words:
            current.append(s[start_idx:start_idx+length])
            for i in range(1, len(words)):
                if s[start_idx + length*i:start_idx + length*(i+1)] in words:    
                    current.append(s[start_idx + length*i:start_idx + length*(i+1)])
                else:
                    break
            if sorted(current) == sorted(words):
                output.append(start_idx)
            current = []

    return output


print(findSubstring("a", ["a"]))