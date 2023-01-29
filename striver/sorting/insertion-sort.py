class Solution:
    def selection_sort(self, arr, n):
        if n == 0 or n == 1:
            return arr
        for i in range(1, n):
            j = i
            while j > 0 and arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                j -= 1
        return arr


arr = [13, 46, 24, 52, 20, 9]
obj = Solution()
sorted_arr = obj.selection_sort(arr, len(arr))
print(sorted_arr)


# here we need to sort an array. We will use the process - take an element and place it at its current place.
# we will start our iteration from 1, because we will check all the elements till 0th from the current position and will swap if the previous item is bigger than the current.
# so will iterate the first for loop from 1 to the last element and the inner for loop from "i"th to the 0.
# on every iteration of the inner for loop we will swap it the previous item is bigger than the current.

# here time complexity of the solution will be - O(n ^ 2) and space complexity will be - O(1).
# as we are iterating the whole array for the n-1 th times and iterating the inner array on every iteration, the time complexity becomes n * n = O(n ^ 2).
# as our temporary storage size is always 1 and doesn't dependent on the size of the array, our space complexity is O(1).

# Note  ::: Here the Best case scenario is - O(n) and the Average case scenario and the Worst case scenario, both are - O(n ^ 2).
# Why Best case scenario is - O(n) ? Because if the array is already sorted, the time complexity will be - O(n).

# Video Link - https://www.youtube.com/watch?v=HGk_ypEuS24
