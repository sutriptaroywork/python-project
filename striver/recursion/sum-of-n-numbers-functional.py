class Solution:
    def sum(self, i):
        if i == 0:
            return 0
        return i + self.sum(i - 1)

    def fact(self, i):
        if i == 1:
            return 1
        return i * self.fact(i - 1)

obj = Solution()
n = 6
sum = obj.sum(n)
fact = obj.fact(n)
print(sum)
print(fact)
