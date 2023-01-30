class Solution:
    def lcsUtil(self, x, y, s1, s2):
        if x == 0 or y == 0:
            return 0

        if (s1[x-1] == s2[y-1]):
            return 1 + self.lcsUtil(x - 1, y - 1, s1, s2)
        else:
            return max(self.lcsUtil(x - 1, y, s1, s2), self.lcsUtil(x, y - 1, s1, s2))
    
    def longest_common_subsequence(self, x, y, s1, s2):
        return self.lcsUtil(x, y, s1, s2)

# Driver code
obj = Solution()
str1 = "ABCDGH"
str2 = "AEDFHR"
n = 6
m = 6
res = obj.longest_common_subsequence(n, m, str1, str2)
print(res) 


# here we need to find the longest common subsequence between two string.
# subsequence is actually a part of a string. It can be any part but not the empty string.
# so here we need to find that how much character is matched between two strings.
# so for we are planning to remove last character and check for the sequence.
# if we have similar character at the end of both the strings, we are adding 1 and doing the same.
# if we have different character at the end of the subsequences, we are going to remove last character from 1st one in 1st case and last character from 2nd one in 2nd case. And we will store the maximum common from those two subsequences.
# we will do a recursive call every time.

# here time complexity of the solution will be - O(2 ^ n) and space complexity will be - O(1).
# as we are dividing the string into 2 different part, the time complexity becomes O(2 ^ n).
# as we are not using any variable to store values, the space complexity will be O(1).


# More Optimized ---


class Solution:
    def lcsUtil(self, x, y, s1, s2, dp):
        if x == 0 or y == 0:
            return 0

        if dp[x][y] != -1:
            return dp[x][y]

        if (s1[x-1] == s2[y-1]):
            dp[x][y] = 1 + self.lcsUtil(x - 1, y - 1, s1, s2, dp)
            return dp[x][y]
        else:
            dp[x][y] = max(self.lcsUtil(x - 1, y, s1, s2, dp), self.lcsUtil(x, y - 1, s1, s2, dp))
            return dp[x][y]
    
    def longest_common_subsequence(self, x, y, s1, s2):
        dp = [[0 for j in range(y+1)] for i in range(x+1)]

        for i in range(1, x+1):
            for j in range(1, y+1):
                dp[i][j] = -1
        return self.lcsUtil(x, y, s1, s2, dp)

# Driver code
obj = Solution()
str1 = "ABCDGH"
str2 = "AEDFHR"
n = 6
m = 6
res = obj.longest_common_subsequence(n, m, str1, str2)
print(res) 


# here we are doing the same, but we are storing the combination every time. So next time whenever we are getting the same combination check between two subsequences, we will return the stored value, rather than checking again.

# here time complexity of the solution will be - O(n * m) and space complexity will be - O(n * m).
# as we are doing the process by storing every combination matching, and next time we are using that rather than doing again, it reduces the time from O(2 ^ n) to O(n * m).
# as we are storing combination matching numbers into a matrix to reuse in future, the space complexity will be O(n * M).

# Video Link - https://www.youtube.com/watch?v=0yvOxPwe3Dg / https://www.youtube.com/watch?v=Ua0GhsJSlWM

