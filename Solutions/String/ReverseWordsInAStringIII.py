def reverseWords(s: str) -> str:
    output = []
    words = ["".join(list(reversed(word))) for word in s.split(" ")]

    return " ".join(words)


print(reverseWords("Let's take LeetCode contest"))