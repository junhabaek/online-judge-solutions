import heapq
from collections import deque

test_graph = {
    'A': {'B': 10, 'C': 2, 'D': 3},
    'B': {},
    'C': {'B': 6, 'D': 3},
    'D': {'E': 4, 'F': 6},
    'E': {'F': 2},
    'F': {'A': 6}
}


def dijkstra(graph, start):
    distance = {dot: float('inf') for dot in graph}
    distance[start] = 0
    heap = []
    heapq.heappush(heap, [distance[start], start])

    path = {dot: start for dot in graph}

    while heap:
        renewed_distance, renewed_dot = heapq.heappop(heap)

        if renewed_distance <= distance[renewed_dot]:
            distance[renewed_dot] = renewed_distance
            for key, value in test_graph[renewed_dot].items():
                if renewed_distance + value < distance[key]:
                    distance[key] = renewed_distance + value
                    heapq.heappush(heap, [distance[key], key])
                    path[key] = renewed_dot

    return distance, path


def print_shortest_path(start, res_path):
    queue = deque()
    for key, value in res_path.items():
        queue.append(key)
        cur_dot = value
        while cur_dot != start:
            queue.append(cur_dot)
            cur_dot = res_path[cur_dot]

        print(start, end='')
        while queue:
            print(queue.pop(), end='')
        print()


result_distance, result_path = dijkstra(test_graph, 'A')
print(result_distance)
print_shortest_path('A', result_path)
