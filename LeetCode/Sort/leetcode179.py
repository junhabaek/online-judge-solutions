from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_nums = [str(i) for i in nums]

        for i in range(1, len(nums)):
            desired_idx = 0
            cur_target = str_nums[i]
            for j in reversed(range(0, i)):
                desired_idx = j
                if self.isLeftLargerThanRight(cur_target, str_nums[j]):
                    str_nums[j + 1] = str_nums[j]
                else:
                    desired_idx = j + 1
                    break
            str_nums[desired_idx] = cur_target

        result = ''.join(str_nums)

        if result[0] == "0":
            return "0"
        else:
            return result

    def isLeftLargerThanRight(self, a: str, b: str) -> bool:
        i = 0

        while i < len(a) and i < len(b):
            if a[i] > b[i]:
                return True
            elif a[i] < b[i]:
                return False
            i += 1

        if len(a) == len(b):
            return False

        if len(a) > len(b):
            return self.isLeftLargerThanRight(a[i:], b[:i])
        else:
            return self.isLeftLargerThanRight(a[:i], b[i:])
