def lengthOfLastWord(self, s: str) -> int:
    splitted = s.strip().split(" ")
    return len(splitted[-1])