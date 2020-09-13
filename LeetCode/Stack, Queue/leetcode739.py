from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        temp_stack = []
        result_stack = [0] * len(T)

        for i in range(len(T)):
            cur_temp = T[i]

            while temp_stack and temp_stack[-1][0] < cur_temp:
                requested_day = temp_stack.pop()
                result_stack[requested_day[1]] = i - requested_day[1]

            temp_stack.append((cur_temp, i))

        return result_stack
