class Solution:
    def sum(self, i, sum):
        if i < 1:
            print(sum)
            return
        self.sum(i - 1, sum + i)

    def fact(self, i, mult):
        if i < 1:
            print(mult)
            return
        self.fact(i - 1, mult * i)

obj = Solution()
n = 6
obj.sum(n, 0)
obj.fact(n, 1)
