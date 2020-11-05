## 문제 출처 : 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/courses/30/lessons/42861

from functools import reduce


def find_min_noncycle_edge(costs, tree_vertex):
    min_edge = [-1, -1, float('inf')]
    for edge in costs:
        if (edge[0] in tree_vertex) ^ (edge[1] in tree_vertex):
            if min_edge[2] > edge[2]:
                min_edge = edge

    return min_edge if min_edge[0] != -1 else None


def solution(n, costs):
    if n == 1:
        return 0

    tree_vertex = set()
    tree_vertex.add(0)
    tree = []

    while len(tree) < n - 1 and costs:
        min_edge = find_min_noncycle_edge(costs, tree_vertex)
        if min_edge == None:
            break
        else:
            tree_vertex.add(min_edge[0])
            tree_vertex.add(min_edge[1])
            tree.append(min_edge)

    answer = reduce(lambda ans, edge: ans + edge[2], tree, 0)
    return answer
