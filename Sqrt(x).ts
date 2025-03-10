function mySqrt(x: number): number {
    for (let i=0; i < x; i++) {
        let diff: number = x - i * i;
        if (diff < 0) {
            return i - 1
        }
    }
    return x;
};