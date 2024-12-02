dic = {}

def climbStairsHelper(self, current, n):
    if current == n: return 1
    if current > n: return 0
    if current in self.dic.keys(): return self.dic[current]
    self.dic[current] = self.climbStairsHelper(current + 1, n) + self.climbStairsHelper(current + 2, n)
    return self.dic[current]

def climbStairs(self, n):
    return self.climbStairsHelper(0, n)