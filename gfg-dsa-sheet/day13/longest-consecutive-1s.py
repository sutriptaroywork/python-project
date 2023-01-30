class Solution:
    def longest_consecutive_1s(self, N):
        consecutive_count = 0
        count = 0
        while N > 0:
            if N % 2 == 1:
                count += 1
                if count > consecutive_count:
                    consecutive_count = count
            else:
                count = 0
            N = N // 2

        return consecutive_count

# Driver code
obj = Solution()
n = 14
res = obj.longest_consecutive_1s(n)
print(res) 


# here we need to find the longest consecutive 1's from the binary representation of a number.
# so we have to convert a number into binary format and we need to maintain the count of 1 in a variable.
# here every time we are getting 1, we are increasing count by 1 and checking if the longest count till now is greater than or not. If not, we are assigning the count.
# every time we are getting 0, the count variable is getting reset to 0.

# here time complexity of the solution will be - O(log n) and space complexity will be - O(1).
# as we are dividing the number by 2, it will take the time like binary search. So the time complexity is - O(log n).
# as we are using variables to store values which are not directly dependent on the size of the array, the space complexity will be O(1).

