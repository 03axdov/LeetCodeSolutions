function isAnagram(s: string, t: string): boolean {
    if (s.length != t.length) return false

    let sortedS: string = s.split("").sort().join("");
    let sortedT: string = t.split("").sort().join("");

    return sortedS == sortedT;
};