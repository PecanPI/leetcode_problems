class Solution:
    def isPalindrome(self, x: int) -> bool:
        string_x = str(x)
        string_x = string_x[::-1]
        if string_x == str(x):
            return True
        return False



sol = Solution()
print(sol.isPalindrome(-121))