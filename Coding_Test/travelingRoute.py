## 문제 출처 : 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/courses/30/lessons/43164

class TravelingRoutes:
    def __init__(self, tickets):
        self.__tickets = tickets
        self.__best_route = []

    def calculate_traveling_route(self):
        self.__best_route = []
        self.find_route(["ICN"], self.__tickets)
        return self.__best_route

    def find_route(self, cur_route, tickets):
        if not tickets:
            if self.__best_route:
                self.__best_route = min(cur_route, self.__best_route)
            else:
                self.__best_route = cur_route
            return

        for idx, move in enumerate(tickets):
            if cur_route[-1] == move[0]:
                self.find_route(cur_route[::] + [move[1]], tickets[:idx] + tickets[idx + 1:])


def solution(tickets):
    travel = TravelingRoutes(tickets)
    answer = travel.calculate_traveling_route()
    return answer
