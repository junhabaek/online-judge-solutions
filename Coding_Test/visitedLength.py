## 문제 출처 : 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/courses/30/lessons/49994

from collections import defaultdict

def is_visited(visited_dict, path):
    return visited_dict[path]

def solution(dirs):
    answer = 0
    last_coord = (0, 0)
    coord = [0,0]

    visited_path_dict = defaultdict(bool)

    for cur_dir in dirs:
        if cur_dir == "L":
            tmp = coord[0]
            coord[0] = tmp - 1 if tmp != -5 else tmp
        elif cur_dir == "R":
            tmp = coord[0]
            coord[0] = tmp + 1 if tmp != 5 else tmp
        elif cur_dir == "U":
            tmp = coord[1]
            coord[1] = tmp + 1 if tmp != 5 else tmp
        else:
            tmp = coord[1]
            coord[1] = tmp - 1 if tmp != -5 else tmp

        coord_tup = tuple(coord)
        if not coord_tup == last_coord:
            path = (coord_tup, last_coord) if coord_tup<= last_coord else (last_coord, coord_tup)
            if not is_visited(visited_path_dict, path):
                answer+=1
                visited_path_dict[path] = True
        last_coord = coord_tup

    return answer
