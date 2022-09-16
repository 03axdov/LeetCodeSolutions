def numberOfWeakCharacters(properties):
    sortedAttack = sorted(properties, key=lambda character: character[0], reverse=True)
    currentMaxDef = sortedAttack[0][1]
    maxDef = 0
    prevAttack = sortedAttack[0][0]

    output = 0
    for character in sortedAttack:
        if prevAttack != character[0]:
            maxDef = max(currentMaxDef, maxDef)
            currentMaxDef = 0
            prevAttack = character[0]

        if character[1] < maxDef:
            output += 1
        
        currentMaxDef = max(currentMaxDef, character[1])

    return output

print(numberOfWeakCharacters(
[[10,1],[5,1],[7,10],[4,1],[5,9],[6,9],[7,2],[1,10]]))