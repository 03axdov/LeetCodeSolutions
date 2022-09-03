class Solution:
    output = []
    def numsSameConsecDiff(self, n: int, k: int):
        self.output = []
        current = ''
        self.generate(current, n, k)

        return self.output

    def generate(self, current, n, k):
        if len(current) == n:
            if self.isValid(current, k):
                self.output.append(int(current))
        else:
            if current:
                newChar1 = int(current[-1]) + k
                newChar2 = int(current[-1]) - k
                if 0 <= newChar1 < 10:
                    self.generate(current + str(newChar1), n, k)
                if 0 <= newChar2 < 10 and newChar2 != newChar1:
                    self.generate(current + str(newChar2), n, k)
            else:
                for i in range(1, 10):
                    self.generate(current + str(i), n, k)

    def isValid(self, current, k):
        l, r = 0, 1
        while r < len(current):
            if int(current[l]) - int(current[r]) != k and int(current[l]) - int(current[r]) != -k: return False
            l, r = l + 1, r + 1
        return True

s = Solution()

print(s.numsSameConsecDiff(2, 1))