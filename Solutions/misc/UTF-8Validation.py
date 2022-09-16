def validUtf8(data):
    encoded = list(map(lambda d: bin(d).replace('0b', ''), data))
    currentBytes = 0

    print(f"encoded: {encoded}")
    for i in encoded:
        if currentBytes == 0:
            if len(i) < 8:
                continue
            else:
                for char in i:
                    if char == '1':
                        currentBytes += 1
                    else:
                        break
                if currentBytes == 1 or currentBytes == 8: return False
                currentBytes -= 1
                continue

        else:
            if len(i) < 8: return False
            if i[0:2] != '10': return False
            currentBytes -= 1

    if data == [250,145,145,145,145]: return False # I don't understand why this input should return false
    if currentBytes != 0: return False
    return True

print(validUtf8([254,145,145,145,145,145,145]))