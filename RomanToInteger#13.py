class Solution:
    def romanToInt(self, s: str) -> int:

        roman_convert= {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        roman_subtract = {'IV': -2, 'IX': -2, 'XL': -20, 'XC': -20, 'CD': -200, 'CM': -200}
        num = 0
        for i in s:
            num += roman_convert[i]
        for i in roman_subtract:
            if i in s:
                num += roman_subtract[i]

        return num


sol = Solution()
print(sol.romanToInt('MCMXCI'))