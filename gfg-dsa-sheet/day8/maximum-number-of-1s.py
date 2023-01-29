class Solution:
    def max_no_of_1s(self, arr, n, m):
        max_no_till_now = 0
        index_with_max_till_now = 0
        for i in range(n):
            if arr[i][0] == 1 and m > max_no_till_now:
                max_no_till_now = m
                index_with_max_till_now = i
                break

            if arr[i][m-1] == 0:
                continue
            
            left = 0
            right = m - 1
            while left < right:
                mid = left + (right - left) // 2

                if arr[i][mid] == 1 and arr[i][mid - 1] == 0:
                    no_of_1s = m - mid
                    if no_of_1s > max_no_till_now:
                        max_no_till_now = no_of_1s
                        index_with_max_till_now = i
                    break
                elif arr[i][mid] == 0:
                    left += 1
                else:
                    right -= 1
        
        return index_with_max_till_now


# Driver code
obj = Solution()
n, m = 3, 4
arr = [[0, 0, 1, 1], [0, 0, 1, 1], [0, 1, 1, 1]]
index_no = obj.max_no_of_1s(arr, n, m)
print(index_no) 


# here we need to find the index on which we have an array with maximum 1s.
# so for that we need to iterate the first array and check the values of second array by using Binary Search ( Note : Our arrays are sorted and contains with only 0s and 1s ).
# first we need to check 2 things. 1) if the first element is 1 or not. if it is, we will add the array length as maximum one. because in a sorted array, if the first element is 1, all the element to the right will be 1.
# next we need to check if the last element of the array is 0 or not. if it is, we will continue and won't check the array as in a sorted array if the last element is 0, all the element is zero.
# if the above two conditions skips, we will check the elements.
# so every time we need to check if the mid point is 1 and the previous item is 0 or not.
# if it is, get the difference to the end from that point. Because in sorted array with 0s and 1s, if we get 1 in any point that means all the right side items will be 1 ).
# now check if the maximum number of 1 till now is less than the current no of 1's or not.
# if it is, we will store the current no of 1's into the maximum no of 1 till now variable and update the index number with maximum 1's with the current index.


# here time complexity of the solution will be - O(n log n) and space complexity will be - O(1).
# as we are iterating the inner arrays through binary search within the outer array or main array, the time is directly dependent upon the size of the arrays. Here the time complexity will be O(n log n).
# as we are using variables to store values which are not directly dependent on the size of the array, the space complexity will be O(1).

# Video Link - https://www.youtube.com/watch?v=tWtq2nd7sI4
