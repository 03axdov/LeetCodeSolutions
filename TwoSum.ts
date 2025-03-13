function twoSum(nums: number[], target: number): number[] {
    let map: Map<number, number> = new Map();
    for (let i=0; i < nums.length; i++) {
        let num: number = nums[i];
        if (map.has(num)) {
            return [map.get(num)!, i]
        }
        map.set(target - num, i);
    }

    return [];
};