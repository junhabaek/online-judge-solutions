class QuadTree:
    def __init__(self, arr):
        self.arr = arr
        self.lines = len(self.arr)

    def get_str_of_full_tree(self):
        return self.get_str_of_subtree(0, 0, lines)

    # 순환 함수형태로 정의
    # square의 한 꼭짓점이 (x_start, y_start)이며 한 변의 길이가 cur_length일 때, 그 사각형 내부의 string을 반환
    def get_str_of_subtree(self, x_start, y_start, cur_length):

        # 1*1 square인 상태
        if cur_length == 1:
            # 현재 채워진 숫자 (0/1)을 반환
            return self.arr[x_start][y_start]
        else:
            divided_length = cur_length // 2

            # 4분할된 각각의 square의 합을 담을 list
            results = []
            results.append(self.get_str_of_subtree(x_start, y_start, divided_length))
            results.append(self.get_str_of_subtree(x_start, y_start + divided_length, divided_length))
            results.append(self.get_str_of_subtree(x_start + divided_length, y_start, divided_length))
            results.append(self.get_str_of_subtree(x_start + divided_length, y_start + divided_length, divided_length))

            concatenated_result = "".join(results)

            # 전부 일치하면 단일 문자 반환
            if len(concatenated_result) == 4:
                if concatenated_result.count(concatenated_result[0]) == 4:
                    return concatenated_result[0]

            # 불일치시 괄호 씌워서 return하기.
            return "(" + concatenated_result + ")"


lines = int(input())
full_array = []

# 배열 채우기
for i in range(lines):
    full_array.append(list(input()))

# lines = 8
# full_array = []
#
# full_array.append(["1", "1", "1", "1", "0", "0", "0", "0"])
# full_array.append(["1", "1", "1", "1", "0", "0", "0", "0"])
# full_array.append(["0", "0", "0", "1", "1", "1", "0", "0"])
# full_array.append(["0", "0", "0", "1", "1", "1", "0", "0"])
# full_array.append(["1", "1", "1", "1", "0", "0", "0", "0"])
# full_array.append(["1", "1", "1", "1", "0", "0", "0", "0"])
# full_array.append(["1", "1", "1", "1", "0", "0", "1", "1"])
# full_array.append(["1", "1", "1", "1", "0", "0", "1", "1"])


problem_solver = QuadTree(full_array)
result_str = problem_solver.get_str_of_full_tree()

print(result_str)

