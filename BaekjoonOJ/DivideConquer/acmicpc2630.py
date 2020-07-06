class ColorSquare:
    # 순환 함수형태로 정의
    # square의 한 꼭짓점이 (x_start, y_start)이며 한 변의 길이가 cur_length일 때, 그 사각형 내부의 숫자 합을 구한다.
    # 맥락상으로 유지되어야 할(함수가 영향을 주는) 변수들의 종류가 많기 때문에 클래스 선언
    def __init__(self, arr):
        self.arr = arr
        self.lines = len(self.arr)
        self.blue_squares = 0
        self.white_squares = 0

    def get_nums_of_colored_squares(self):
        self.blue_squares = 0
        self.white_squares = 0

        full_square_area = self.get_sum_of_square(0, 0, lines)
        if full_square_area == 0:
            self.white_squares = self.white_squares + 1
        elif full_square_area == lines * lines:
            self.blue_squares = self.blue_squares + 1

        return self.blue_squares, self.white_squares

    # 초기 호출형태는 full_array, 0, 0, lines
    def get_sum_of_square(self, x_start, y_start, cur_length):

        # 1*1 square인 상태
        if cur_length == 1:
            # 현재 채워진 숫자 (0/1)을 반환
            return self.arr[x_start][y_start]
        else:
            divided_length = cur_length // 2

            # 4분할된 각각의 square의 합을 담을 list
            results = []
            results.append(self.get_sum_of_square( x_start, y_start, divided_length))
            results.append(self.get_sum_of_square( x_start + divided_length, y_start, divided_length))
            results.append(self.get_sum_of_square( x_start, y_start + divided_length, divided_length))
            results.append(self.get_sum_of_square( x_start + divided_length, y_start + divided_length, divided_length))

            sum_of_results = sum(results)

            cur_full_area = cur_length * cur_length

            if not (sum_of_results == 0 or sum_of_results == cur_full_area):

                for sub_area in results:
                    if sub_area == 0:
                        self.white_squares = self.white_squares + 1
                    elif sub_area == cur_full_area // 4:
                        self.blue_squares = self.blue_squares + 1

            return sum_of_results


lines = int(input())
full_array = []

# 배열 채우기
for i in range(lines):
    full_array.append(list(map(int, input().split())))

# lines = 8
# full_array = []
#
# full_array.append([1, 1, 0, 0, 0, 0, 1, 1])
# full_array.append([1, 1, 0, 0, 0, 0, 1, 1])
# full_array.append([0, 0, 0, 0, 1, 1, 0, 0])
# full_array.append([0, 0, 0, 0, 1, 1, 0, 0])
# full_array.append([1, 0, 0, 0, 1, 1, 1, 1])
# full_array.append([0, 1, 0, 0, 1, 1, 1, 1])
# full_array.append([0, 0, 1, 1, 1, 1, 1, 1])
# full_array.append([0, 0, 1, 1, 1, 1, 1, 1])

problem_solver = ColorSquare(full_array)
blue_squares, white_squares = problem_solver.get_nums_of_colored_squares()

print(white_squares)
print(blue_squares)

