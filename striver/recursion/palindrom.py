class Solution:
    def check_palindrome(self, i, n, str):
        if i >= n:
            return True
        if str[i] != str[n]:
            return False
        return self.check_palindrome(i + 1, n - 1, str)

obj = Solution()
str = "madam"
n = 5
i = 0
is_palindrome = obj.check_palindrome(i, n-i-1, str)
print(is_palindrome)
