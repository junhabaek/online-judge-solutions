from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        str_logs = []
        number_logs = []

        for cur_log in logs:
            if cur_log.split()[1].isdigit():
                number_logs.append(cur_log)
            else:
                str_logs.append(cur_log)

        str_logs.sort(key=lambda cur_log: (cur_log.split()[1:],
                                           cur_log.split()[0]))

        str_logs.extend(number_logs)
        return str_logs
