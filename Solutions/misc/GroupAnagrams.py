def groupAnagrams(strs):
    dic = {}
    
    for string in strs:
        sortedLetters = "".join(sorted(string))
        if sortedLetters in dic.keys():
            dic[sortedLetters].append(string)
        else:
            dic[sortedLetters] = [string]
        
    return dic.values().map(list)