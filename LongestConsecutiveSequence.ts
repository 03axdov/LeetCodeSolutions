function longestConsecutive(nums: number[]): number {
    let numSet: Set<number> = new Set(nums);
    let res: number = 0;

    for (let i=0; i < nums.length; i++) {
        let num: number = nums[i];
        if (!numSet.has(num)) continue;

        let currentLength: number = 1;
        let j: number = 1;
        while (numSet.has(num + j)) {
            currentLength += 1;
            numSet.delete(num + j);
            j += 1;
        }
        j = 1;
        while (numSet.has(num - j)) {
            currentLength += 1;
            numSet.delete(num - j);
            j += 1;
        }

        res = Math.max(res, currentLength)
    }

    return res;
};