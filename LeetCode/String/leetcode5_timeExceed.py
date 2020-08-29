class Solution:
    def longestPalindrome(self, s: str) -> str:
        str_len = len(s)
        left_index, right_index = 0, str_len - 1

        left_str = []
        right_str = []

        max_len = 0
        cur_max_str = ""

        while left_index <= str_len - 1:
            while left_index <= right_index:
                if s[left_index] == s[right_index]:
                    temp_left, temp_right = left_index, right_index
                    middle_char = ""
                    while temp_left <= temp_right:
                        if s[temp_left] == s[temp_right]:
                            if temp_left == temp_right:
                                middle_char = s[temp_left]
                                break
                            else:
                                left_str.append(s[temp_left])
                                temp_left = temp_left + 1
                                right_str.append(s[temp_right])
                                temp_right = temp_right - 1
                        else:
                            left_str = []
                            right_str = []
                            break

                    cur_str = ''.join(left_str) + middle_char + ''.join(right_str[::-1])
                    left_str = []
                    right_str = []

                    if len(cur_str) > max_len:
                        cur_max_str = cur_str
                        max_len = len(cur_str)

                right_index = right_index - 1

            left_index = left_index + 1
            right_index = str_len - 1

        return cur_max_str


# sol = Solution()
# result = sol.longestPalindrome("babad")
# print(result)
