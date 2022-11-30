class Solution:
    def find_uncommon(self, str1, str2):
        char_list = ""
        freq1 = {}
        freq2 = {}

        for i in range(26):
            freq1[i] = False
            freq2[i] = False


        str1_char_list = list(str1)
        str2_char_list = list(str2)

        for i in str1_char_list:
            freq1[ord(i) - ord('a')] = True

        for i in str2_char_list:
            freq2[ord(i) - ord('a')] = True

        
        for i in range(26):
            if freq1[i] ^ freq2[i]:
                char_list += chr(ord('a') + i)

        if char_list == "":
            return -1

        return char_list


str2 = "geeksforgeeks"
str1 = "geeksquiz"
obj = Solution()
uncommon_char_list = obj.find_uncommon(str1, str2)
print(uncommon_char_list)


# we need to find all the uncommon characters from the two strings.
# here we are first taking two constant hashmaps of 26 items with all the value - "False".
# as english can have maximum 26 characters, we are taking the length of 26.
# then we are iterating two loops to get all the characters of the two strings.
# then everytime, we are getting the distance of the character from "a" by subtracting the ASCII code of "a" from the ASCII code of that character.
# everytime we are storing "True" to the item in hashmap with that difference.
# at the end, we are comparing both the hashmaps by using XOR checking.
# XOR returns "true", if both are different.
# So if a charactar is true in one of those two hashmaps, then only it will give true.
# if it is present or missing in both the cases i.e. same in both the cases, it returns false.
# so trough this we can able to acheive the different characters of the two strings.


# so here space complexity = O(1) and time complexity = O(n + m) i.e. O(n).
# n + m ≤ n + n = 2n, which is O(n). Thus O(n+m) = O(n).
# as there is no nested for loop, the time complexity will be O(n + m) i.e. the length of two arrays i.e. O(n).
# as we are using two hashmaps which have a length of 26 each, the length of the hashmap is fixed. so the space complexity is constant i.e. O(1). 
