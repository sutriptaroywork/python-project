class Solution:
    def sort_0s_1s_2s(self, arr):
        l, mid, r = 0, 0, arr.length - 1

        while mid <= r:
            if arr[mid] == 0:
                arr[l], arr[mid] = arr[mid], arr[l]
                l += 1
                mid += 1
            elif arr[mid] == 1:
                mid += 1
            else
                arr[r], arr[mid] = arr[mid], arr[r]
                r -= 1

        return arr


arr = [0, 2, 1, 2, 0, 1]

obj = Solution()
sorted_arr = obj.sort_0s_1s_2s(arr)
print(sorted_arr)


# here we are trying to sort an array of items in 0,1,2 manner.
# as we need to track all the different types and we have three types of items, we are taking 3 different variables to store the track.
# to achieve that, we will iterate the array by using a while loop untill our 3rd variable or highest variable becomes same with midium variable of 2nd variable.
# we will check the array item that is pointing by the "mid" variable everytime.
# if it is 0, we will swap the low and mid positioned item and increase both the variable by 1.
# if it is 1, we will just increase the mid variable by 1 and do nothing.
# if we get 2, we will swap high and mid positioned items and decrease high by 1.

# so here space complexity = O(1) and time complexity = O(n).
# as we are not using any extra space, it will be a space complexity of O(1).
# as we are iterating the array once, the time complexity will be O(n).
