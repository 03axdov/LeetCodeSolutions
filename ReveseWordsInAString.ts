function reverseWords(s: string): string {
    let words: string[] = s.split(" ").filter((w) => {return w.length > 0}).reverse()

    return words.join(" ");
};