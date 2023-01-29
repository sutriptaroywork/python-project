class Solution:
    def distinct_every_window(self, A, N, K):
        res = []
        my_map = {}
        for i in range(N):
            if i >= k:
                first_key = A[i - k]
                first_key_val = my_map[first_key]

                if first_key_val == 1:
                    del my_map[first_key]
                else:
                    count = my_map[first_key]
                    count -= 1
                    my_map[first_key] = count

            if my_map.get(A[i]):
                count = my_map[A[i]]
                count += 1
                my_map[A[i]] = count
            else:
                my_map[A[i]] = 1

            if i >= K - 1:
                res.append(len(my_map))

        return res


# Driver code
obj = Solution()
arr = [1, 2, 1, 3, 4, 2, 3]
k = 4
# arr = [78, 16, 94, 36, 87, 93, 50, 22, 63, 28, 91, 60, 64, 27]
# k = 5
res = obj.distinct_every_window(arr, len(arr), k)
print(res) 


# here we need to find the count of distinct numbers in every window.
# so we have a window number which is stored into a variable named "k" and we have an array of numbers.
# so we have to check that for every "k" numbers of items in the array how many distinct numbers are there.
# for getting the distinct numbers, we need store the numbers into a dictionary or hashmap.
# now on every iteration we are checking that if the "i" is greater than or equal to the "k". If it is we are checking the distinct and adding that into the array and removing or decreasing the counter of the older key, which is less than "i-k".

# here time complexity of the solution will be - O(n) and space complexity will be - O(n).
# as we are iterating the array, the time is directly dependent upon the size of the array. Here the time complexity will be O(n).
# as we are using variables to store values which are directly dependent on the size of the array, the space complexity will be O(n).

# Video Link - https://www.youtube.com/watch?v=j48e8ac7r20
