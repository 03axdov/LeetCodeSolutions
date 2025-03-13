function findPeakElement(nums: number[]): number {
    let l: number = 0;
    let r: number = nums.length - 1;

    while (l < r) {
        let mid: number = Math.floor((l + r) / 2);

        if (nums[mid] > nums[mid + 1]) {
            r = mid
        } else {
            l = mid + 1
        }
    }

    return l;
};