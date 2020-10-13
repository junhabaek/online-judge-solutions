from collections import Counter
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = Counter(nums)

        idx = 0
        for k, v in sorted(cnt.items()):
            for i in range(v):
                nums[idx] = k
                idx += 1

