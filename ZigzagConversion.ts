function convert(s: string, numRows: number): string {
    if (numRows == 1) return s;
    let rows: string[][] = new Array();
    for (let i=0; i < numRows; i++) {
        rows.push([]);
    }
    let currentRow = 0;
    let dirDown: boolean = true;

    for (let i=0; i < s.length; i++) {
        let c: string = s[i];
        rows[currentRow].push(c);
        currentRow += (dirDown ? 1 : -1)
        if (currentRow == numRows - 1) dirDown = false
        if (currentRow == 0) dirDown = true;
    }

    return rows.map((row) => row.join("")).join("");
};