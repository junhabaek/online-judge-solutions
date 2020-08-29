from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        left_idx, right_idx, max_idx = 0, 1, len(nums) - 1

        result_list = []

        while left_idx < max_idx - 1:
            right_idx = left_idx + 1
            while right_idx < max_idx:
                target = -(nums[left_idx] + nums[right_idx])
                if target in nums[right_idx + 1:]:
                    cur_result = [nums[left_idx], nums[right_idx], target]
                    cur_result.sort()

                    if cur_result not in result_list:
                        result_list.append(cur_result)

                right_idx = right_idx + 1
            left_idx = left_idx + 1
        return result_list
