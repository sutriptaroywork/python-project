# Top - Down Approach ( Recursion )

# class Solution:
#     def calculate_cost(self, n, cost):
#         if n <= 1:
#             return cost[n]

#         return cost[n] + min(self.calculate_cost(n-1, cost), self.calculate_cost(n-2, cost))

#     def nth_step_cost(self, cost):
#         n = len(cost)
#         return min(self.calculate_cost(n-1, cost), self.calculate_cost(n-2, cost))


# cost = [10, 15, 30]
# obj = Solution()
# total_cost = obj.nth_step_cost(cost)
# print(total_cost)

# NOTE --- T.C = O(2 ^ N), S.C = O(1) ( As we are calling the function 2 times -  self.dataBuilder(n-1) + self.dataBuilder(n-2), time complexity is - 2^N)

##############################################################################

# Top - Down Approach ( Recursion + Memoization )

# class Solution:
#     def calculate_cost(self, n, cost, my_list):
#         if n <= 1:
#             return cost[n]

#         if my_list[n] != -1:
#             return my_list[n]

#         my_list[n] = cost[n] + min(self.calculate_cost(n-1, cost, my_list), self.calculate_cost(n-2, cost, my_list))
#         return my_list[n]

#     def nth_step_cost(self, cost):
#         n = len(cost)
#         my_list = list(-1 for i in range(n+1))
#         return min(self.calculate_cost(n-1, cost, my_list), self.calculate_cost(n-2, cost, my_list))


# cost = [10, 15, 30]
# obj = Solution()
# total_cost = obj.nth_step_cost(cost)
# print(total_cost)

# NOTE --- T.C = O(N), S.C = O(N) + O(N)

##############################################################################

# Bottom - Up Approach ( Tabulation )

# class Solution:
#     def nth_step_cost(self, cost):
#         n = len(cost)
#         my_list = []
#         for i in range(n):
#             if i <= 1:
#                 my_list.append(cost[i])
#             else:
#                 my_list.append(cost[i] + min(my_list[i-1], my_list[i-2]))

#         return min(my_list[n-1], my_list[n-2])

# cost = [10, 15, 30]
# obj = Solution()
# total_cost = obj.nth_step_cost(cost)
# print(total_cost)

# NOTE --- T.C = O(N), S.C = O(N)

##############################################################################

# Bottom - Up Approach ( Tabulation ) with less space complexity

class Solution:
    def nth_step_cost(self, cost):
        n = len(cost) 
        prev2 = cost[0]
        prev = cost[1]
        
        for i in range(2, n):
            curr = cost[i] + min(prev, prev2)
            prev2 = prev
            prev = curr

        return min(prev, prev2)


cost = [10, 15, 30]
obj = Solution()
total_cost = obj.nth_step_cost(cost)
print(total_cost)

# NOTE --- T.C = O(N), S.C = O(1)
