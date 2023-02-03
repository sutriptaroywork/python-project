class Solution:
    def recursion(self, i, n):
        if i > n:
            return
        print(i)
        i += 1
        self.recursion(i, n)

obj = Solution()
n = 6
obj.recursion(1, n)
