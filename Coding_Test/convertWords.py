## 문제 출처 : 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/courses/30/lessons/43163

class WordConverter:
    def __init__(self, begin, target, words):
        self.__begin = begin
        self.__target = target
        self.__words = words
        self.__steps = float('inf')

    def able_go_futher(self, before_word, after_word):
        same_chr = 0
        for i in range(len(before_word)):
            if before_word[i] == after_word[i]:
                same_chr += 1

        return True if same_chr == len(before_word) - 1 else False

    def get_min_steps(self):
        self.__steps = float('inf')
        self.find_step(self.__begin, self.__words, 0)
        return self.__steps if self.__steps <= 50 else 0

    def find_step(self, last, possible_choices, steps):
        if last == self.__target:
            if steps < self.__steps:
                self.__steps = steps
                return
        if not possible_choices:
            return

        for idx, word in enumerate(possible_choices):
            if self.able_go_futher(last, word):
                self.find_step(word, possible_choices[:idx] + possible_choices[idx + 1:], steps + 1)


def solution(begin, target, words):
    cvt = WordConverter(begin, target, words)
    answer = cvt.get_min_steps()
    return answer
