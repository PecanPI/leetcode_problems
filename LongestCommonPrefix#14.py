from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return''
        strs.sort()
        for i,(a,b) in enumerate(zip(strs[0], strs[-1])):
            if a != b:
                return strs[0][:i]

        return strs[0] # if it goes through the loop the last and first word are the same up
                        # to the length of the first word


sol = Solution()
print(sol.longestCommonPrefix(["flower", "flow", "flight"]))
print(sol.longestCommonPrefix(["dog", "racecar", "car"]))
print(sol.longestCommonPrefix([]))
print(sol.longestCommonPrefix(["aaa", "aa", "aaa"]))
print(sol.longestCommonPrefix(["cb", "cbb", "a"]))