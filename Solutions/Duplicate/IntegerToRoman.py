def intToRoman(num: int) -> str:
    mapping = [(1000, "M"), (500, "D"), (100, "C"), (50, "L"), (10, "X"), (5, "V"), (1, "I")]
    subtractiveForm = [(900, "CM"), (400, "CD"), (90, "XC"), (40, "XL"), (9, "IX"), (4, "IV")]
    
    res = ""
    while num > 0:
        print(num)
        if str(num)[0] == "9" or str(num)[0] == "4":
            for pair in subtractiveForm:
                if pair[0] <= num:
                    res += pair[1]
                    num -= pair[0]
                    break
        else:
            for pair in mapping:
                if pair[0] <= num:
                    res += pair[1]
                    num -= pair[0]
                    break
            
    return res

print(intToRoman(3749))