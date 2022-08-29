from collections import Counter
def canConstruct(ransomNote: str, magazine: str) -> bool:
    ransomNoteLetters = Counter(ransomNote)
    magazineLetters = Counter(magazine)
    for (key, value) in ransomNoteLetters.items():
        if magazineLetters[key] >= value:
            continue
        else:
            return False
    return True


canConstruct('aaabb', 'aab')