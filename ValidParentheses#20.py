from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True

        number_of_parethesis = {'(': 0, ')': 0, '{': 0, '}': 0, '[': 0, ']': 0}
        queue = deque()

        for i in range(len(s)):
            if

sol = Solution()
print(sol.isValid(''))