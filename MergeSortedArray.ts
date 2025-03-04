function merge(nums1: number[], m: number, nums2: number[], n: number): void {
    let idx: number = 0;

    while (nums2.length > 0) {
        if (nums2[0] < nums1[idx] || idx >= m) {
            let temp = nums1[idx];
            nums1[idx] = nums2.shift()!;
            if (idx < m) {
                nums2.push(temp);
                nums2.sort((a, b) => {
                    return a - b;
                });
            };
            
        }

        idx += 1;
    }
};