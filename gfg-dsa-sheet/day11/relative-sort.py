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


# here we need to sort the first array according to the second array i.e we need to add all the items from the first array which matches with the second array and then add the remaining items in sorted order. If no item from second array matches with the first array just return first array in a sorted manner.
# so we need to sort the first array.
# then we need to use a hashmap to store the items of the first array with its occurrence.
# then we need to find the items from second array one by one from the hashmap and need to add those in a separate array fo r the times it occurs in the first array and delete those keys from the hashmap.
# and then we need to add the remaining keys for the times it occurs in the first array and delete every item from the hashmap.

# here time complexity of the solution will be - O(n log n) and space complexity will be - O(n).
# as we are sorting the array and then iterating the array, we have a time complexity of sorting - O(n log n).
# as we are using hashmap to store values which is directly dependent on the size of the array, the space complexity will be O(n).

