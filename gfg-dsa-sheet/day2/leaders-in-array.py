class Solution:
    def leader_in_array(self, arr):
        leaders_arr = []
        max_till_now  =-1
        n = len(arr)

        for i in reversed(range(n)):
            if arr[i] > max_till_now:
                leaders_arr.append(arr[i])
                max_till_now = arr[i]
            
        leaders_arr.reverse()
        return leaders_arr


arr = [16, 17, 4, 3, 5, 2]
obj = Solution()
reverse_arr = obj.leader_in_array(arr)
print(reverse_arr)


# here we need to find the leaders from the array.
# we have to add the numbers which are greater than all the elements of its right side.
# to implement this, we will use the logic of reverse iteration.
# we will iterate the array from the last and evertime we will get the maximum we will push it in our array and store into an variable.
# let's understand this with an example.
# ex - arr = [16, 17, 4, 3, 5, 2]. So the output will be - [17, 5, 2].
# as the last element has no other item to compare, we assume it a leader than all the items of it's right.
# we will take -1 as our initial max value, so that the last element satisfy the conditional check.


# here time complexity of the solution will be - O(n) and space complexity will be - O(n).
# as we are itersting the array, so time is directly dependant on the size of array. So the time complexitry will be O(n).
# as we are using an array of items which dependant on the number of items the array has, it will be a space complexity of O(n).
