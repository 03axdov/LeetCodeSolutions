function isPalindrome(s: string): boolean {
    s = s.toLowerCase();
    const lowercaseLetters: Set<string> = new Set("abcdefghijklmnopqrstuvwxyz1234567890");
    s = s.split("").filter((c) => lowercaseLetters.has(c)).join("");

    let midpoint: number = s.length / 2;

    let latterHalfStart: number;
    if (s.length % 2 == 1) {
        latterHalfStart = midpoint + 1;
    } else {
        latterHalfStart = midpoint;
    }

    let firstHalf: string = s.substring(0, midpoint);
    let latterHalf: string = s.substring(latterHalfStart, s.length);

    let i1: number = firstHalf.length - 1;
    let i2: number = 0;

    while (i1 >= 0 && i2 < latterHalf.length) {
        if (firstHalf[i1] !== latterHalf[i2]) return false;
        i1 -= 1;
        i2 += 1;
    }

    return true;
};