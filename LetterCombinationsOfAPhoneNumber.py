def letterCombinations(self, digits):
    mapping = {"2": "abc", "3": "def", "4": "ghi",
               "5": "jkl", "6": "mno", "7": "pqrs",
               "8": "tuv", "9": "wxyz"}
    
    res = []
    
    for digit in digits:
        if len(res) == 0:
            for letter in mapping[digit]: res.append(letter)
        else:
            resCopy = res.copy()
            res = []
            for letter in mapping[digit]:
                for prevComb in resCopy:
                    res.append(prevComb + letter)
                    
    return res