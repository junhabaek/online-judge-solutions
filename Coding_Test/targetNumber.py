## 문제 출처 : 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/courses/30/lessons/43165

class TargetNumber:
    def __init__(self, numbers, sum_list, target_level, target_number):
        self.__numbers = numbers
        self.__sum_list = sum_list
        self.__target_level = target_level
        self.__target_number = target_number
        self.__result_count = 0

    def init_get_sum(self):
        self.__result_count = 0
        self.get_sum(0, 0)
        return self.__result_count

    def get_sum(self, k, last_sum):
        if k == self.__target_level:
            if last_sum == self.__target_number:
                self.__result_count += 1
            return

        added = last_sum + self.__numbers[k]
        subtracted = last_sum - self.__numbers[k]

        if added + self.__sum_list[k + 1] >= self.__target_number \
                or added - self.__sum_list[k + 1] <= self.__target_number:
            self.get_sum(k + 1, added)
        if subtracted + self.__sum_list[k + 1] >= self.__target_number \
                or subtracted - self.__sum_list[k + 1] <= self.__target_number:
            self.get_sum(k + 1, subtracted)


def solution(numbers, target):
    numbers.sort(reverse=True)
    max_range = sum(numbers)
    sum_list = [max_range]

    for idx in range(len(numbers)):
        max_range -= numbers[idx]
        sum_list.append(max_range)

    tg = TargetNumber(numbers, sum_list, len(numbers), target)

    answer = tg.init_get_sum()
    return answer
