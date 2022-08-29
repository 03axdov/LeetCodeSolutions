def letterCombinations(digits):
    output = []
    current = []
    nums = {'2':'abc', '3':'def',
            '4':'ghi', '5':'jkl',
            '6':'mno', '7':'pqrs',
            '8':'tuv', '9':'wxyz'}
    for digit in digits:
        letters = nums[digit]
        if len(output) == 0:
            for letter in letters:
                current.append(letter)
        else:
            for letter in letters:
                for sequence in output:
                    current.append(sequence + letter)
        output = current
        current = []
    
    return output

print(letterCombinations("2"))