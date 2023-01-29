class Solution:
    def relative_sort(self, A1, N, A2, M):
        A1.sort()
        my_map = {}
        res = []

        for i in range(N):
            if my_map.get(A1[i]) is None:
                my_map[A1[i]] = 1
            else:
                count = my_map[A1[i]]
                count += 1
                my_map[A1[i]] = count

        for i in range(M):
            if my_map.get(A2[i]) is not None:
                count = my_map[A2[i]]
                del my_map[A2[i]]
                while count > 0:
                    res.append(A2[i])
                    count -= 1

        remaining_keys = list(my_map.keys())

        for i in remaining_keys:
            count = my_map[i]
            del my_map[i]
            while count > 0:
                res.append(i)
                count -= 1

        return res


# Driver code
obj = Solution()
# arr1 = [2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8]
# arr2 = [2, 1, 8, 3]
# n = 11
# m = 4
arr1 = [45, 15, 23, 8, 5, 12, 26, 444, 888, 151, 12, 23, 45, 15, 56]
arr2 = [15, 888, 444, 5, 8, 12, 23]
n = 15
m = 7
res = obj.relative_sort(arr1, n, arr2, m)
print(res) 


# here we need to find the maximum number of toys we can buy.
# we have an array of prices of the toys.
# so we need to add lowest value toys to add maximum number of toys within the "k" amount of money.
# so we need to sort the array first to get the lowest amounts first.
# and then we are just checking that if the price is less than or equal to the money, no of toys is getting increased by 1 and total money is getting decreased by the price of the toy.

# here time complexity of the solution will be - O(n log n) and space complexity will be - O(1).
# as we are sorting the array and then iterating the array, we have a time complexity of sorting - O(n log n) and a time complexity of iterating - O(n). So adding both becomes O(n log n) + O(n) = O(n log n). Because we always ignore the lower time complexity.
# as we are using variables to store values which are not directly dependent on the size of the array, the space complexity will be O(1).

