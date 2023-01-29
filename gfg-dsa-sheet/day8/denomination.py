# find the denomination
# if not found then return the nearest lower and upper denomination

class Solution:
    def nearest_denomination(self, arr, d):
        left = 0
        right = len(arr) - 1

        low = left
        high = right

        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] == d:
                return [d]
            elif arr[mid] < d:
                low = arr[left]
                left += 1
            else:
                right -= 1
                high = arr[right]
        return [low, high]

# Driver code
obj = Solution()
arr = [5, 10, 15, 22, 33, 40, 42, 55]
d = 25
index_no = obj.nearest_denomination(arr, d)
print(index_no) 


# here we need to find the denomination or to get the previous and next values of the denomination.
# as our denomination array is sorted, we will find the the denomination through the binary search.
# so if we get the denomination we will return the index number.
# else if the mid is less than the denomination, we will store the left value as the low and increase the left value by 1.
# else if the mid value is greater than the denomination, we will first decrease our right value by 1 and store as the high.
# at the end we will return the low and high.

# here time complexity of the solution will be - O(log n) and space complexity will be - O(1).
# as we are iterating the array using binary search, the time complexity will be O(log n).
# as we are using variables to store values, which are not directly dependent on the size of the array, the space complexity will be O(1).

