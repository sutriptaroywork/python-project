class Solution:
    def power_of_2(self, n):
        if n == 0:
            return False
        if n == 1:
            return True

        while n > 1:
            if n % 2 == 1:
                return False
            n = n // 2

        return True

# Driver code
obj = Solution()
n = 0
res = obj.power_of_2(n)
print(res) 


# here we need to find the that the integer is a power of 2 or not.
# so if we observe in a proper way, we will find that, every number which are the power of 2 is always divisible by 2 with a remainder of 0.
# ex - 32 is the power of 2. 2 ^ 5 = 32. If we divide 32 by 2, it will give 16, remainder 0. Then 16 / 2 = 8, again remainder 0. This is because 32 has made by multiplying 2 every time. So dividing by 2, will be always with 0 remainder.
# this concept we will use to find if the number is the power of 2 or not.
# so whenever we encounter a remainder of 1, we will return False, else we will continue to divide until the number gets 1.
# here we need to handle two edge cases before the loop. We need to return False if the number is 0, and return True if the number is 1.

# here time complexity of the solution will be - O(log n) and space complexity will be - O(1).
# as we are dividing the number by 2 every time, it will take the time like binary search. So the time complexity is - O(log n).
# as we are not using any variable, the space complexity will be O(1).

# Video Link - https://www.youtube.com/watch?v=4cqHahxFTYw
