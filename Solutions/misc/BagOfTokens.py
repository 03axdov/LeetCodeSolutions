def bagOfTokensScore(tokens, power: int) -> int:
    tokens = sorted(tokens)
    score = 0
    currentPower = power
    l, r = 0, len(tokens) - 1

    while l <= r:
        print(f"Token: {tokens[l]}, currentPower: {currentPower}, score: {score}")
        if tokens[l] <= currentPower:
            print("A")
            currentPower -= tokens[l]
            score += 1
        if score != 0  and l < r - 1 and tokens[l + 1] > currentPower:
            print("B")
            score -= 1
            currentPower += tokens[r]
            r -= 1
        l += 1
        print("")

    return score


print(bagOfTokensScore([100], 150))