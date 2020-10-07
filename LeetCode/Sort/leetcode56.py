class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []

        sorted_intervals = sorted(intervals)

        result_list = []
        latter_idx = 1
        cur_range = sorted_intervals[0][:]

        while latter_idx < len(sorted_intervals):
            latter = sorted_intervals[latter_idx][:]
            if latter[0] <= cur_range[1] <= latter[1]:
                cur_range = [cur_range[0], latter[1]]
            elif cur_range[0] <= latter[0] and cur_range[1] >= latter[1]:
                cur_range = [cur_range[0], cur_range[1]]
            else:
                result_list.append(cur_range)
                cur_range = latter

            latter_idx += 1

        result_list.append(cur_range)

        return result_list
