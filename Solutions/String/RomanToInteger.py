def romanToInt(s):
    numerals = {'I': 1, 'V': 5, 'X': 10,
                'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    output = 0
    for i in range(len(s)):
        if i != 0:
            if s[i] == 'V' and s[i-1] == 'I' or s[i] == 'X' and s[i-1] == 'I':
                output += numerals[s[i]] - 2
            elif s[i] == 'L' and s[i-1] == 'X' or s[i] == 'C' and s[i-1] == 'X':
                output += numerals[s[i]] - 20
            elif s[i] == 'D' and s[i-1] == 'C' or s[i] == 'M' and s[i-1] == 'C':
                output += numerals[s[i]] - 200
            else:
                output += numerals[s[i]]
        else:
            output += numerals[s[i]]
    
    return output


print(romanToInt("MCMXCIV"))