function isSubsequence(s: string, t: string): boolean {
    if (!s || s.length > t.length) return true
    let l1 = 0;
    let l2 = 0;
    let r1= s.length - 1;
    let r2 = t.length - 1;

    while (l1 <= r1 && l2 <= r2) {
        if (s[l1] == t[l2]) {
            l1 += 1;
            l2 += 1
        }
        l2 += 1

        if (s[r1] == t[r2]) {
            r1 -= 1;
        }
        r2 -= 1;
        
    }

    return l1 > r1;
};