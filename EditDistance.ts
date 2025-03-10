function minDistance(word1: string, word2: string): number {
    let distance: number = Math.abs(word1.length - word2.length);
    let toRemove: number = distance;

    let longerWord: string = (word1.length > word2.length ? word1 : word2);
    let shorterWord: string = (word1.length > word2.length ? word2 : word1);

    let longerWordChars: Map<string, number> = new Map<string, number>();
    for (let i=0; i < longerWord.length; i++) {
        let char = longerWord[i]
        if (!longerWordChars.has(char)) longerWordChars.set(char, 1);
        else longerWordChars.set(char, longerWordChars.get(char)! + 1);
    }

    for (let i=0; i < shorterWord.length; i++) {
        let char = shorterWord[i];
        if (longerWordChars.has(char)) {
            if (longerWordChars.get(char)! <= 0) {
                if (toRemove <= 0) distance += 1
                toRemove -= 1 
            }
            
            longerWordChars.set(char, longerWordChars.get(char)! - 1)
        } else {
            if (toRemove <= 0) distance += 1
            toRemove -= 1
        }
    }

    return distance;
};