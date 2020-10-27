## 문제 출처 : 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/courses/30/lessons/12979

import math


def calculate_expansion_count(leftmax_uncovered_area, rightmax_uncovered_area, w):
    new_station_count = 0
    if leftmax_uncovered_area <= rightmax_uncovered_area:
        uncovered_count = rightmax_uncovered_area - leftmax_uncovered_area + 1
        new_station_count += math.ceil(uncovered_count / (2 * w + 1))
    return new_station_count


def solution(n, stations, w):
    answer = 0
    last_uncovered_area = 1

    for station in stations:
        answer += calculate_expansion_count(last_uncovered_area, station - w - 1, w)
        last_uncovered_area = station + w + 1

    answer += calculate_expansion_count(last_uncovered_area, n, w)

    return answer
