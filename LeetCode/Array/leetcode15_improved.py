from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result_list = []
        nums.sort()

        for i in range(len(nums) - 2):
            target = nums[i]
            left_idx, right_idx = i + 1, len(nums) - 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while left_idx < right_idx:
                left_val, right_val = nums[left_idx], nums[right_idx]

                if left_val + right_val == -target:
                    result_list.append([left_val, right_val, target])

                    while left_idx < right_idx and nums[left_idx] == nums[left_idx + 1]:
                        left_idx = left_idx + 1

                    while left_idx < right_idx and nums[right_idx] == nums[right_idx - 1]:
                        right_idx = right_idx - 1

                    left_idx = left_idx + 1
                    right_idx = right_idx - 1

                cur_sum = left_val + right_val + target
                if cur_sum < 0:
                    left_idx = left_idx + 1
                elif cur_sum > 0:
                    right_idx = right_idx - 1

        return result_list
