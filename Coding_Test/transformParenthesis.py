## 문제 출처 : 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/courses/30/lessons/60058


def split_balanced_str(target_str):
    left_count = 0
    right_count = 0
    split_index = -1

    for index, s in enumerate(target_str):
        if s == '(':
            left_count += 1
        else:
            right_count += 1
        if left_count == right_count:
            split_index = index
            break
    if split_index == -1:
        split_index = len(target_str) - 1
    return target_str[:split_index + 1], target_str[split_index + 1:]


def is_correct_parenthesis(target_str):
    left_count = 0
    right_count = 0

    for s in target_str:
        if s == '(':
            left_count += 1
        else:
            right_count += 1
        if right_count > left_count:
            return False

    return True


def get_opposite_parenthesis(target_str):
    result = []
    for s in target_str:
        if s == '(':
            result.append(')')
        else:
            result.append('(')
    return ''.join(result)


def get_correct_parenthesis(target_str):
    if len(target_str) == 0:
        return ''
    u, v = split_balanced_str(target_str)

    if is_correct_parenthesis(u):
        return u + get_correct_parenthesis(v)
    else:
        return '(' + get_correct_parenthesis(v) + ')' + get_opposite_parenthesis(u[1:-1])


def solution(p):
    if len(p) == 0:
        return ''
    elif is_correct_parenthesis(p):
        return p

    return get_correct_parenthesis(p)