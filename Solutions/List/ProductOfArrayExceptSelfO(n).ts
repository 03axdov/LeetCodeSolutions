function productExceptSelfOn(nums: number[]): number[] {
    let trailing: Map<number, number> = new Map();
    let current: number = 1;
    for (let i=nums.length - 1; i >= 0; i--) {
        trailing.set(i, current);
        current *= nums[i];
    }

    let res: number[] = [];
    current = 1;
    for (let i=0; i < nums.length; i++) {
        res.push(current * trailing.get(i)!);
        current *= nums[i];
    }

    return res;
};