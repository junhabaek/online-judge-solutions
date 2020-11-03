## 문제 출처 : 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    cits = sorted(citations, reverse=True)

    max_h = 0
    for idx, cit in enumerate(cits):
        if idx + 1 > cits[idx]:
            break

        cur_h = idx + 1
        if cur_h > max_h:
            max_h = cur_h

    return max_h

# test_data = [3,0,6,1,5]
# print(solution(test_data))
