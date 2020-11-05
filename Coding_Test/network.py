## 문제 출처 : 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/courses/30/lessons/43162

class ConnectComponent:
    def __init__(self, array, n):
        self.__array = array
        self.__n = n
        self.__visited = [False for _ in range(n)]

    def calculate_component_count(self):
        cnt = 0

        cur_stk = []
        for i in range(self.__n):
            if self.__visited[i] == False:
                cur_stk.append(i)
                cnt += 1
                while cur_stk:
                    cur_val = cur_stk.pop()
                    if self.__visited[cur_val] == True:
                        continue
                    self.__visited[cur_val] = True
                    for j in range(self.__n):
                        if self.__visited[j] == False and self.__array[cur_val][j] == 1:
                            cur_stk.append(j)

        return cnt


def solution(n, computers):
    con_comp = ConnectComponent(computers, n)
    answer = con_comp.calculate_component_count()

    return answer
