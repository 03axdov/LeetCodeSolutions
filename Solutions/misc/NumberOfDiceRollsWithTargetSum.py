class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        memoization = {}

        def traversal(depth, rem):
            if depth == n:
                if rem == 0: return 1
                return 0

            if rem <= 0: return 0

            if (depth, rem) in memoization:
                return memoization[(depth, rem)]

            combinations = 0
            for i in range(1, k+1):
                combinations += traversal(depth+1, rem-i)
            memoization[(depth, rem)] = combinations % (10**9 + 7)

            return memoization[(depth, rem)]
        

        return traversal(0, target)