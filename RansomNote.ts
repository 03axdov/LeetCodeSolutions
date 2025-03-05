function canConstruct(ransomNote: string, magazine: string): boolean {
    let map: Map<string, number> = new Map();

    for (let i=0; i < magazine.length; i++) {
        let char: string = magazine[i];
        if (map.has(char)) {
            map.set(char, map.get(char)! + 1);
        } else {
            map.set(char, 1);
        }
    }

    for (let i=0; i < ransomNote.length; i++) {
        let char: string = ransomNote[i];
        if (!map.has(char)) return false;
        else {
            map.set(char, map.get(char)! - 1);
            if (map.get(char)! < 0) return false;
        }
    }

    return true;
};