class Solution:
    def minimum_indexed_character(self, str, patt):
        str_arr = list(str)
        patt_arr = list(patt)
        lowest_index = -1
        my_map = {}

        for i in range(len(str_arr)):
            if my_map.get(str_arr[i]) is None:
                my_map[str_arr[i]] = i
        
        for i in range(len(patt_arr)):
            if my_map.get(patt_arr[i]) is not None:
                index = my_map[patt_arr[i]]
                if lowest_index == -1 or index < lowest_index:
                    lowest_index = index
        return lowest_index


# Driver code
obj = Solution()
# str = "geeksforgeeks"
# patt = "set"

str = "hasjkhflaskdf"
patt = "sdlkjfshd"
# arr = [78, 16, 94, 36, 87, 93, 50, 22, 63, 28, 91, 60, 64, 27]
# k = 5
res = obj.minimum_indexed_character(str, patt)
print(res)


# here we need to find the lowest index which matched with any of the character present in the pattern string.
# so first we have to use hashmap or dictionary to store all the unique characters with their index.
# if any character is coming 2nd time, we ignore, bcz we need the index where the character occurred first.
# then we will check every character of the pattern and check its index from the hashmap we already have stored.
# if no character found from the hashmap, we will return -1, else we will return the lowest index we are getting from all the characters.

# Note ::: Here on the second loop, I have used "is not None" to check the item is present or not. Why ? Because if I was using normal "my_map.get(patt_arr[i])", it was returning the value stored, which is "0", because "h" first occurs on "0". So the check was getting failed every time.

# here time complexity of the solution will be - O(n) and space complexity will be - O(n).
# as we are iterating the array, the time is directly dependent upon the size of the array. Here the time complexity will be O(n).
# as we are using variables to store values which are directly dependent on the size of the array, the space complexity will be O(n).

