from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left_index, right_index = 0, len(height) - 1
        left_height, right_height = 0, 0

        while left_index < len(height):
            if height[left_index] > 0:
                left_height = height[left_index]
                break
            left_index = left_index + 1

        while right_index >= 0:
            if height[right_index] > 0:
                right_height = height[right_index]
                break
            right_index = right_index - 1

        if (left_index == right_index) or (left_index == len(height)):
            return 0

        volume = 0

        while left_index != right_index:
            if left_height >= right_height:
                right_index = right_index - 1
                if right_height >= height[right_index]:
                    volume = volume + (right_height - height[right_index])
                else:
                    right_height = height[right_index]
            else:
                left_index = left_index + 1
                if left_height >= height[left_index]:
                    volume = volume + (left_height - height[left_index])
                else:
                    left_height = height[left_index]

        return volume
