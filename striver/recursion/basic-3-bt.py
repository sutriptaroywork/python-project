class Solution:
    def recursion(self, i, n):
        if i < 1:
            return
        self.recursion(i - 1, n)
        print(i)

obj = Solution()
n = 6
obj.recursion(n, n)
