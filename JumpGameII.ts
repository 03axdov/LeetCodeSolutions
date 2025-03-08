function jump(nums: number[]): number {
    let jumps: number[] = Array(nums.length).fill(Infinity);
    jumps[0] = 0;

    for (let i=0; i < nums.length; i++) {
        let current: number = nums[i];

        for (let j=i; j < Math.min(nums.length, i + current + 1); j++) {
            jumps[j] = Math.min(jumps[j], 1 + jumps[i])
        }
    }

    return jumps[jumps.length - 1];
};