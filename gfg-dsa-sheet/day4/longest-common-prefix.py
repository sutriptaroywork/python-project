class Solution:
    def longest_common_prefix(self, arr):
        common_prefix = ""

        for i in range(len(arr[0])):
            for s in arr:
                if i == len(s) or s[i] != arr[0][i]:
                    if common_prefix == "":
                        return -1
                    return common_prefix
            common_prefix += arr[0][i]

        if common_prefix == "":
            return -1
        return common_prefix


arr = ["geeksforgeeks", "geeks", "geek", "geezer"]
# arr = ["geeks", "geeks", "geeks", "geeks"]

obj = Solution()
common_prefix = obj.longest_common_prefix(arr)
print(common_prefix)


# here we need to find the longest common prefix.
# so we have to match all the strings letter by letter and once we get uncommon letter in any of the strings, we return the common prefix till now.
# if common prefix till now is empty, we need to return -1.
# also at the end we will return the common prefix, if empty, we will return -1.
# the implementation plan will be quite similar but a bit confusing at first.
# we will use two for loops. In first for loop, we will take the length of the first item of the array and run a for loop.
# in second for loop we will loop all the the words and check with the "i" position letter from each of the words.
# if we find that the "i" is the length of any of the words or "i" the positioned letter of any of the word is not matching with the 0th word's "i"th letter, we will return common prefix till now by checking empty.
# if we don't find any uncommon on any of the words "i"th letter, we will add the "i"th letter of the 0th word after the inner for loop.
# why after the inner for loop ? because we need to complete the checking of each of the words "i"th letter and if no uncommon letter happens in any of the word, then only we need to add the letter after the inner for loop.


# here time complexity of the solution will be - O(n^2) and space complexity will be - O(n).
# as we are iterating two for loops, one for the first word and another for the main array, time complexity is directly dependent on the length of the first word and the array. So the time complexity will be O(n^2).
# as we are storing common prefix into a variable where the length of the variable is dependent on the length of the common prefix for the words in the given array, the space complexity will be O(n).
