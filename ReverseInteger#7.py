class Solution:
    def reverse(self, x: int) -> int:
            if x >= 0:
                string_int = str(x)
                reverse_int = string_int[::-1]
                if int(reverse_int) < (2**31 - 1):
                    return int(reverse_int)
                else:
                    return 0
            else:
                string_int = str(x)
                reverse_int = string_int[:0:-1]
                if -1 * int(reverse_int) > (-(2 ** 31)):
                    return -1 * int(reverse_int)
                else:
                    return 0




sol = Solution()
print(sol.reverse(-2147483648))