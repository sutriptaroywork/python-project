class Solution:
    def maximize_toys(self, arr, N , K):
        no_of_toys = 0

        arr.sort()

        for i in range(N):
            if arr[i] <= K:
                no_of_toys += 1
                K -= arr[i]

        return no_of_toys


# Driver code
obj = Solution()
arr = [1, 12, 5, 111, 200, 1000, 10]
n = 7
k = 50
res = obj.maximize_toys(arr, n, k)
print(res) 


# here we need to find the maximum number of toys we can buy.
# we have an array of prices of the toys.
# so we need to add lowest value toys to add maximum number of toys within the "k" amount of money.
# so we need to sort the array first to get the lowest amounts first.
# and then we are just checking that if the price is less than or equal to the money, no of toys is getting increased by 1 and total money is getting decreased by the price of the toy.

# here time complexity of the solution will be - O(n log n) and space complexity will be - O(1).
# as we are sorting the array and then iterating the array, we have a time complexity of sorting - O(n log n).
# as we are using variables to store values which are not directly dependent on the size of the array, the space complexity will be O(1).

