## 문제 출처 : 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/courses/30/lessons/42579
from collections import defaultdict


def solution(genres, plays):
    answer = []

    plays_per_genre = defaultdict(list)
    cumul_plays_per_genre = defaultdict(int)

    for i in range(len(genres)):
        cumul_plays_per_genre[genres[i]] += plays[i]
        plays_per_genre[genres[i]].append((plays[i], i))

    for genre in sorted(cumul_plays_per_genre.keys(), key=lambda x: -cumul_plays_per_genre[x]):
        answer.extend(tup[1] for tup in sorted(plays_per_genre[genre], key=lambda x: (-x[0], x[1]))[:2])

    return answer
