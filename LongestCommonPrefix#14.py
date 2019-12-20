from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        strs.sort()
        prefix = strs[0]
        long_prefix = ""
        for i in strs:
            k = 0
            for j in i:
                try:
                    if j == prefix[k]:
                        long_prefix += j
                        k += 1
                    else:
                        break
                except:
                    return long_prefix
            prefix = long_prefix
            long_prefix = ""

        return prefix


sol = Solution()
print(sol.longestCommonPrefix(["flower", "flow", "flight"]))
print(sol.longestCommonPrefix(["dog", "racecar", "car"]))
print(sol.longestCommonPrefix([]))
print(sol.longestCommonPrefix(["aaa", "aa", "aaa"]))
print(sol.longestCommonPrefix(["cb", "cbb", "a"]))