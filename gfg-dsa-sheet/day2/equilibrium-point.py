class Solution:
    def equilibrium_point(self, arr):
        n = len(arr)
        if n == 0:
            return 0

        if n == 1:
            return 1

        sum_of_all = sum(arr)

        left_sum = 0
        for i in range(n):
            right_sum = sum_of_all - left_sum - arr[i]
            if left_sum == right_sum:
                return i + 1
            left_sum += arr[i]
            
        return -1


arr = [3, 8, 12, 6, 5]
obj = Solution()
equilibrium_item = obj.equilibrium_point(arr)
print(equilibrium_item)


# here we are going to find the equilibrium point in an array.
# so what is equilibrium point in an array is ?
# it is the point, where the sum of all the right items and the sum of all the left items are same.
# let's understand with an example.
# ex - arr = [3, 8, 12, 6, 5]. So here the equilibrium point is 3. That means the item on the 3rd position i.e. 12.
# if we check closely, we can find that the sum of 3 + 8 = 11 and also the sum of 6 + 5 = 11. So 12 is the equilibrium point.
# it can be same for arr = [3, 8, 12, 11].
# as here also on the 3rd position, we have 12 and sum of both the sides i.e. sum of the right elements and sum of the left elements are 11.
# so here the 3rd position is an equilibrium point.

# here the time complexity is - O(n) and space complexity is - O(1).
# as we are iterating the array only once, so the time is directly dependant on the size of the array. So the time complexirty is O(n).
# as we are taking variables to store the sum, the size of the variable is not dependant on the size of the array. It is constant. So we have a space complexity of - O(1).
