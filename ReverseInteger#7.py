class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            string_int = str(x)
            reverse_int = string_int[::-1]
            return int(reverse_int)
        else:
            string_int = str(x)
            reverse_int = string_int[:0:-1]
            print(reverse_int)
            return -1 * int(reverse_int)


sol = Solution()
print(sol.reverse(-123))