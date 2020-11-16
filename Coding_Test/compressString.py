## 문제 출처 : 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/courses/30/lessons/60057


def get_num_of_digits(num):
    if num == 1:
        return 0
    result = 1
    temp = num
    while temp >= 10:
        temp = temp // 10
        result += 1
    return result


def solution(s):
    min_length_list = [len(s) for _ in range(len(s) // 2 + 1)]

    for unit_length in range(1, len(s) // 2 + 1):
        cur_unit = s[:unit_length]
        cur_duplicate_count = 0
        for unit_start_point in range(unit_length, len(s) - unit_length + 1, unit_length):
            compare_target_unit = s[unit_start_point:unit_start_point + unit_length]
            if compare_target_unit == cur_unit:
                cur_duplicate_count += 1
            else:
                min_length_list[unit_length] += get_num_of_digits(cur_duplicate_count + 1)
                min_length_list[unit_length] -= cur_duplicate_count * unit_length
                cur_unit = compare_target_unit
                cur_duplicate_count = 0

        min_length_list[unit_length] += get_num_of_digits(cur_duplicate_count + 1)
        min_length_list[unit_length] -= cur_duplicate_count * unit_length

    return min(min_length_list)