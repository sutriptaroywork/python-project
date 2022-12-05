class Solution:
    def subarray_given_sum(self, arr, target):
        current_sum = arr[0]
        start = 0
        i = 1
        while i <= len(arr):
            while current_sum > target and start < i - 1:
                current_sum -= arr[start]
                start += 1

            if current_sum == target:
                return [start + 1, i]

            if i < len(arr):
                current_sum += arr[i]

            i += 1

        return -1


arr = [1, 2, 3, 7, 11]
target = 12
obj = Solution()
index = obj.subarray_given_sum(arr, target)
print(index)


# here we need to find a subarray where the sum of the items will be the given sum.
# ex - given sum = 12, given array = [1, 2, 3, 7, 11]. So here [2, 3, 7] this is a sub array which has a sum of 12.
# the array consists of only non-negative numbers, so that we can check like this.
# so we have to take a sum variable with an initial value of 0 and we have to take a variable to store the start point.
# then we need to iterate the array and everytime we need to add the item with the sum variable and check if it is exceeding the target value.
# if the sum is exceeding the target value, we need to remove items from the starting point one by one untill the sum becomes less than or equal to the target.
# whenever we get the target, just return the starting point and the current point.


# here time complexity of the solution will be - O(n) and space complexity will be - O(1).
# as we are iterating the whole array, the time is directly dependent on the size of the array. So the time complexity will be O(n).
# as we are storing only the starting point that doesn't dependent on the size of the array, the space complexity will be O(1).



# Notes :
#      1) here we are starting for loop from 1 because we are initially taking 0th element as current sum.
#      2) then we are adding 1 with start as we are returning the starting item no, not index no. So 2nd index means 3rd item. As we are returning the item, we are adding 1 with the starting position.
#      3) then we are sending ending position without adding 1, because we are checking the sum till the (i - 1)th element. If not matching then only we are adding "i"th element. So here the index is "i - 1" and item is "i - 1 + 1", that means "i".
#      4) then we are adding "i" th item, if it is less than the array length. This we need to check as we are running the array till (array length + 1)th item.
#      5) now why we are running array till (array length + 1)th item ? because we need to check the sum after adding the last item. Now after adding the last item, there is no checking happeing. So we are running the iteration till (array length + 1)th item.
#      6) now why we are checking before addition ? because we are taking 0th item as current sum initially, if it not matches with the target, then only we add the next item.
#      7) in the while loop we are running the loop till the less of the previous item of the current item i.e. "i - 1". Because we are not still added last item, so it won't be less than i. As the sum already happens till the previous item, we are taking till 1 item less than the previous item.
