from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        for i in range(len(nums) // 2):
            result = result + nums[i * 2]

        return result
