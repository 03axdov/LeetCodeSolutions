function maxProfit(prices: number[]): number {
    let current = 0;
    for (let i=1; i < prices.length; i++) {
        current += Math.max(0, prices[i] - prices[i-1])
    }

    return current;
};