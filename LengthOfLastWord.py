def lengthOfLastWord(self, s: str) -> int:
    splitted = s.split(" ")
    parsed = list(filter(lambda w: w != " ", splitted))
    return len(parsed[-1])