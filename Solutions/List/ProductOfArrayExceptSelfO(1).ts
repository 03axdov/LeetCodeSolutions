function productExceptSelf(nums: number[]): number[] {
    let res: number[] = Array(nums.length).fill(0);

    let current: number = 1;
    for (let i=nums.length - 1; i >= 0; i--) {
        res[i] = current;
        current *= nums[i];
    }


    current = 1;
    for (let i=0; i < nums.length; i++) {
        res[i] *= current;
        current *= nums[i];
    }

    return res;
};