class Solution:
    def swap(self, i, n, arr):
        temp = arr[n]
        arr[n] = arr[i]
        arr[i] = temp
    def reverse(self, i, n, arr):
        if i >= n:
            return
        self.swap(i, n, arr)
        self.reverse(i + 1, n - 1, arr)

obj = Solution()
arr = [1, 7, 5, 0, 11]
n = 5
i = 0
obj.reverse(i, n-i-1, arr)
print(arr)
