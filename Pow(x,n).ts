function myPow(x: number, n: number): number {
    if (x === 0) {
        return 0;
    }
    
    if (n === 0) {
        return 1;
    }

    if (n < 0) {
        return 1 / myPow(x, - n);
    }

    let half = myPow(x, Math.floor(n / 2));

    if (n % 2 == 0) {
        return half * half;
    } else {
        return half * half * x;
    }
};