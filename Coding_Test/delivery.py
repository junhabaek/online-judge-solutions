## 문제 출처 : 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/courses/30/lessons/12978
from collections import defaultdict

def solution(N, road, K):
    answer = 0

    graph = {}
    for i in range(1, N+1):
        graph[i] = defaultdict(lambda: float('inf'))


    for cur_path in road:
        if graph[cur_path[0]][cur_path[1]] > cur_path[2]:
            graph[cur_path[0]][cur_path[1]] = cur_path[2]
            graph[cur_path[1]][cur_path[0]] = cur_path[2]

    path = graph[1].copy()
    path[1] = 0

    appended = [False for _ in range(N+1)]
    appended[1] = True

    for _ in range(N-1):
        next_town = min(path.items(), key=lambda x:x[1] if appended[x[0]] == False else float('inf'))
        appended[next_town[0]] = True

        for i in range(2, N+1):
            if not appended[i]:
                if path[i] > next_town[1] + graph[next_town[0]][i]:
                    path[i] = next_town[1] + graph[next_town[0]][i]

    for i in range(1, N+1):
        if path[i] <= K:
            answer+=1

    for key, value in path.items():
        print(key, value)

    return answer
