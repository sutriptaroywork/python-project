class Solution:
    def selection_sort(self, arr, n):
        if n == 0 or n == 1:
            return arr
        for i in reversed(range(1, n)):
            is_swap = 0
            for j in range(n - 1):
                if arr[j] > arr[j + 1]:
                    is_swap = 1
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
            if is_swap == 0:
                break
        return arr


arr = [13, 46, 24, 52, 20, 9]
obj = Solution()
sorted_arr = obj.selection_sort(arr, len(arr))
print(sorted_arr)


# here we need to sort an array. We will use the process - maximum to the last using adjacent swapping.
# on the first iteration, we will start from 0th position and will go till to the last element.
# we will check the "i"th item and the "i+1"th item and if the "i"th element is greater than the "i+1"th, we will swap it.
# through this we will find our highest element at the end of the array.
# next time we will iterate till n - 1 as we have already placed the highest element at the end.
# the rest of the process is same and on the time we will iterate till 1 less than the present.
# through this, we are placing the highest at the end on every iteration and achieving our target.

# here time complexity of the solution will be - O(n ^ 2) and space complexity will be - O(1).
# as we are iterating the whole array for the n-1 th times to set the highest number at the last index of the sub array, the time complexity becomes n * n = O(n ^ 2).
# as our temporary storage size is always 1 and doesn't dependent on the size of the array, our space complexity is O(1).

# Note  ::: Here the Best case scenario is - O(n) and the Average case scenario and the Worst case scenario, both are - O(n ^ 2).
# Why Best case scenario is - O(n) ? Because if the array is already sorted, the time complexity will be - O(n).

# Video Link - https://www.youtube.com/watch?v=HGk_ypEuS24
