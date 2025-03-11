function merge(intervals: number[][]): number[][] {
    intervals.sort((i1,i2) => i1[0] - i2[0])

    console.log(intervals)

    for (let i=1; i < intervals.length; i++) {
        let current: number[] = intervals[i];
        let prev: number[] = intervals[i-1];
        if (current[0] <= prev[1]) {
            current[0] = prev[0];
            current[1] = Math.max(current[1], prev[1])
            intervals[i-1] = [];
        }
    }

    return intervals.filter((i) => i.length > 0);
};

console.log(merge([[1,3],[2,6],[8,10],[15,18]]))