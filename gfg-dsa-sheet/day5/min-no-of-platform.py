class Solution:
    def min_no_of_platforms(self, arr, dep):
        arr.sort()
        dep.sort()

        i = 0
        j = 0
        max_platform = 0
        count = 0

        while i < len(arr):
            if arr[i] < dep[j]:
                count += 1
                max_platform = max(max_platform, count)
                i += 1
            else:
                count -= 1
                j += 1

        return max_platform


arr = ["0900", "0940", "0950", "1100", "1500", "1800"]
dep = ["0910", "1200", "1120", "1130", "1900", "2000"]
obj = Solution()
no_of_platforms = obj.min_no_of_platforms(arr, dep)
print(no_of_platforms)


# here we need to find the number of minimum platform needed to accommodate all the trains.
# so we have two arrays, one for arrival times and another for departure times.
# so we need to compare all the arrival and departure times.
# we will start this by sorting both the array first, because we need only arrival and departure, not train wise arrival and departure.
# now just take two variables for storing indexing for two arrays and increase when it is bigger than other.
# every time we need to increase the count if arrival time is bigger and decrease the count when the departure time is bigger.
# every time you are increasing count, check if it is bigger than the maximum value, store it into the maximum to track the maximum platform.


# here time complexity of the solution will be - O(n log n) and space complexity will be - O(1).
# as we are sorting both the arrays and then iterating, the time is directly dependent upon the size of the array and the sorting time. So the time complexity will be O(n log n) + O(n), which is O(n log n), as we always take the bigger one.
# as we are using variables to store data where the number of variables is not directly dependent on the size of the array, the space complexity will be O(1).
