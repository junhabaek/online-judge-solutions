## 문제 출처 : 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/courses/30/lessons/42885
def solution(people, limit):
    answer = 0
    duo_left_idx, duo_right_idx = 0, len(people) - 1
    people.sort()

    while duo_left_idx <= duo_right_idx:
        if people[duo_left_idx] + people[duo_right_idx] <= limit:
            duo_left_idx += 1
        duo_right_idx -= 1
        answer += 1

    return answer
