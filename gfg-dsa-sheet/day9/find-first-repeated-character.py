class Solution:
    def first_repeated_character(self, str):
        str_arr = list(str)
        my_map = {}

        for i in range(len(str_arr)):
            if my_map.get(str_arr[i]) is None:
                my_map[str_arr[i]] = 1
            else:
                return str_arr[i]

        return -1


# Driver code
obj = Solution()
str = "geeksforgeeks"
res = obj.first_repeated_character(str)
print(res) 


# here we need to find the first character which is repeating.
# so we need to take a hashmap and ever time we are adding characters into the hashmap, we need to check if it is present or not.
# if not just add that, else return the character.
# after completing the loop return -1, as if we not get any repeated character, then only the loop will be completed.

# here time complexity of the solution will be - O(n) and space complexity will be - O(n).
# as we are iterating the array, the time is directly dependent upon the size of the array. Here the time complexity will be O(n).
# as we are using variables to store values which are directly dependent on the size of the array, the space complexity will be O(n).

