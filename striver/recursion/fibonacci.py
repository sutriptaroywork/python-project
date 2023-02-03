class Solution:
    def fibonacci(self, i, j, n):
        k = i + j
        if (k > n):
            return
        print(k)
        self.fibonacci(j, k ,n)

obj = Solution()
n = 100
i = 0
j = 1
obj.fibonacci(i, j, n)
