import collections

class Solution:
    def rearrange_with_max_min(self, arr):
        n = len(arr)
        max_element = arr[n - 1] + 1

        min = 0
        max = n - 1

        for i in range(n):
            if i % 2 == 0:
                arr[i] = arr[i] + (arr[max] % max_element) * max_element
                max -= 1
            else:
                arr[i] = arr[i] + (arr[min] % max_element) * max_element
                min += 1

        for i in range(n):
            arr[i] = arr[i] // max_element

        return arr


arr = [1, 2, 3, 4, 5, 6]
obj = Solution()
maximum_array = obj.rearrange_with_max_min(arr)
print(maximum_array)


# here we need to alter the array with max-min process i.e [max, min, max, min, ........]  like this.
# so to do this we will use a formula where we will take a number that is maximum than the last index.
# as it is a sorted array, the last element is the maximum of all the elements. So to take maximum than the last is to add at least 1 with the final element. ( Note : We can add any number except 0 ).
# then we store this new max element into a variable and iterate the array.
# on every iteration, we will check if the index is even or odd.
# if the index is even, we will use the following formula - arr[i] = arr[i] + (arr[max] % max_element) * max_element.
# if the index is odd, we will use the following formula - arr[i] = arr[i] + (arr[min] % max_element) * max_element.
# using these formulas, we will store data into all the indexes first.
# then we will again iterate and divide the values in each of the indexes by the max_element and store the quotient in each indexes.


# here time complexity of the solution will be - O(n) and space complexity will be - O(1).
# as we are iterating, the time is directly dependent upon the size of the array. So the time complexity will be O(n).
# as we are using variable to store only max_element which is constant and not dependent on the size of the array, the space complexity will be O(1).

# Video Link - https://www.youtube.com/watch?v=oK0FKG5kigo
