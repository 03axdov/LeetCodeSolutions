def isIsomorphic(s, t):
    lettersS = {}

    for i in range(len(s)):
        if t[i] not in lettersS.keys():
            if s[i] not in lettersS.values():
                lettersS[t[i]] = s[i]
            else:
                return False
        elif lettersS[t[i]] == s[i]:
            continue
        else:
            return False

    return True


print(isIsomorphic("paper", "title"))