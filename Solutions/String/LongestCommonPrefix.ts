function longestCommonPrefix(strs: string[]): string {
    if (strs.length == 0) return ""

    let res: string = "";
    for (let i=0; i < strs[0].length; i++) {
        res += strs[0][i]
        for (let j=0; j < strs.length; j++) {
            if (!strs[j].startsWith(res)) return res.slice(0, res.length - 1)
        }
    }

    return res;
};