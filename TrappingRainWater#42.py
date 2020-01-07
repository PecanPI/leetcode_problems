from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        current_height = max(height)
        rain_water = 0
        while current_height > 0:
            left_pos = -1
            right_pos = -1
            height_count = -1
            for i in range(len(height)):
                if height[i] >= current_height:
                    height_count += 1
                if height[i] == current_height:
                    if left_pos == -1:
                        left_pos = i
                    else:
                        right_pos = i
            if right_pos != -1:
                rain_water += right_pos - left_pos -height_count
            elif right_pos == left_pos:
                rain_water = rain_water*2
            current_height -= 1

        return rain_water

sol = Solution()

print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(sol.trap([]))
print(sol.trap([2,0,2]))