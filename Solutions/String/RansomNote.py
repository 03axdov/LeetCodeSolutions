def canConstruct(ransomNote, magazine):
    wcRansom = {}
    wcMagazine = {}
    
    for letter in ransomNote:
        if letter not in wcRansom.keys(): wcRansom[letter] = 1
        else:
            wcRansom[letter] += 1
            
    for letter in magazine:
        if letter not in wcMagazine.keys(): wcMagazine[letter] = 1
        else:
            wcMagazine[letter] += 1
            
            
    for letter in wcRansom.keys():
        if letter not in wcMagazine.keys() or wcRansom[letter] < wcMagazing[letter]:
            return False
        
    return True