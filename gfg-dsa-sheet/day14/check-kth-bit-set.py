class Solution:
    def check_kth_bit_set(self, n, k):
        # count = 0
        # while count <= k:
        #     if count == k:
        #         remainder = n % 2
        #         if remainder == 1:
        #             return True
        #     n = n // 2
        #     count += 1

        # return False

        # using bit masking
        if (n & (1 << k)):
            return True
        return False

# Driver code
obj = Solution()
n = 52
k = 3
res = obj.check_kth_bit_set(n, k)
print(res) 


# here we need to find the k th positioned binary digit and check that it is 1 or not.
# so for that, we need to divide the number upto kth times and on kth time, we need to check if the remainder is 1 or not.

# here time complexity of the solution will be - O(k + 1) and space complexity will be - O(1).
# as we are starting from 0 and iterating till kth times, the time complexity is - O(k + 1).
# as we are using variable, which has a constant size, the space complexity will be O(1).

# Video Link - https://www.youtube.com/watch?v=ldhT2uVSdUQ / https://www.youtube.com/watch?v=xFWgZ5DTjFo
