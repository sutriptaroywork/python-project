class Solution:
    def recursion(self, i):
        if i < 1:
            return
        print(i)
        i -= 1
        self.recursion(i)

obj = Solution()
n = 6
obj.recursion(n)
