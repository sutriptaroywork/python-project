class Solution:
    def selection_sort(self, arr, n):
        if n == 0 or n == 1:
            return arr
        for i in range(n - 1):
            smallest = i
            for j in range(i + 1, n):
                if arr[j] < arr[smallest]:
                    smallest = j
            if smallest != i:
                arr[i], arr[smallest] = arr[smallest], arr[i]
        return arr


arr = [13, 46, 24, 52, 20, 9]
obj = Solution()
sorted_arr = obj.selection_sort(arr, len(arr))
print(sorted_arr)


# here we need to sort an array. We will use the process - minimum to the first by using get the minimum and swap it.
# every time we will check the whole array and take the smallest and place on the first position or "i" th position.
# so first we will find the smallest and place on the 0th place, them "i" will be increased to 1.
# now we will find the minimum from 1th to nth position sub array and place the smallest on 1th position or "i"th position, then "i" will be increased to 2nd position.
# the same process will be happened until "i" get the "n-2"th position.
# because on "n-1"th position or last position will automatically hold the highest as we are placing the minimum number on "i"th every time.

# here time complexity of the solution will be - O(n ^ 2) and space complexity will be - O(1).
# as we are iterating to get the swapping position every time and iterating the rest items from that position to the last item on every time to get the smallest from the rest, we are iterating n numbers, nth times. So the time complexity becomes n * n = O(n ^ 2).
# as our temporary storage size is always 1 and doesn't dependent on the size of the array, our space complexity is O(1).

# Note  ::: Here the Best case scenario, the Average case scenario and the Worst case scenario, all are - O(n ^ 2).

# Video Link - https://www.youtube.com/watch?v=HGk_ypEuS24
