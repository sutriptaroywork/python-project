# Top - Down Approach ( Recursion )

# class Solution:
#     def dataBuilder(self, n):
#         if n <= 1:
#             return n

#         return self.dataBuilder(n-1) + self.dataBuilder(n-2)

#     def fib(self, n):
#         return self.dataBuilder(n)


# n = 6
# obj = Solution()
# nth_fib = obj.fib(n)
# print(nth_fib)

# NOTE --- T.C = O(2 ^ N), S.C = O(1) ( As we are calling the function 2 times -  self.dataBuilder(n-1) + self.dataBuilder(n-2), time complexity is - 2^N)

##############################################################################

# Top - Down Approach ( Recursion + Memoization )

# class Solution:
#     def dataBuilder(self, n, dp):
#         if n <= 1:
#             return n

#         if dp[n] != -1:
#             return dp[n]

#         dp[n] = self.dataBuilder(n-1, dp) + self.dataBuilder(n-2, dp)
#         return dp[n]

#     def fib(self, n):
#         my_list = list(-1 for i in range(n+1))
#         return self.dataBuilder(n, my_list)


# n = 6
# obj = Solution()
# nth_fib = obj.fib(n)
# print(nth_fib)

# NOTE --- T.C = O(N), S.C = O(N) + O(N)

##############################################################################

# Bottom - Up Approach ( Tabulation )

# class Solution:
#     def fib(self, n): 
#         my_list = []
#         for i in range(n+1):
#             if i <= 1:
#                 my_list.append(i)
#             else:
#                 my_list.append(my_list[i-1] + my_list[i-2])

#         return my_list[n]

# n = 6
# obj = Solution()
# nth_fib = obj.fib(n)
# print(nth_fib)

# NOTE --- T.C = O(N), S.C = O(N)

##############################################################################

# Bottom - Up Approach ( Tabulation ) with less space complexity

class Solution:
    def fib(self, n): 
        prev2 = 0
        prev = 1
        curr = prev + prev2
        
        for i in range(2, n+1):
            curr = prev + prev2
            prev2 = prev
            prev = curr

        return curr


n = 6
obj = Solution()
nth_fib = obj.fib(n)
print(nth_fib)

# NOTE --- T.C = O(N), S.C = O(1)
