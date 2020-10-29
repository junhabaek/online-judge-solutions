## 문제 출처 : 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/courses/30/lessons/42584

import heapq


def solution(prices):
    n_of_prices = len(prices)
    answer = [0 for _ in range(n_of_prices)]

    h = []
    for i, price in enumerate(prices):
        heapq.heappush(h, (-price, i))
        while h and h[0][0] < -price:
            target = heapq.heappop(h)
            answer[target[1]] = i - target[1]

    while h:
        target = heapq.heappop(h)
        answer[target[1]] = n_of_prices - target[1] - 1
    return answer