oven_depth, dough_counts = map(int, input().split())
oven_radius_list = list(map(int, input().split()))
dough_radius_list = list(map(int, input().split()))

oven_index = oven_depth - 1

# 평탄화 지름 = 맨 처음 지름
flattening_radius = oven_radius_list[0]

for non_flattened_oven_index in range(oven_depth):
    # 현재 지름이 평탄화 지름보다 크거나 같다면
    if oven_radius_list[non_flattened_oven_index] >= flattening_radius:
        # 현재지름 = 평탄화지름
        oven_radius_list[non_flattened_oven_index] = flattening_radius
    else:
        # 아니라면 평탄화지름 = 현재지름
        flattening_radius = oven_radius_list[non_flattened_oven_index]

# 평탄화 결과 체크
# for i in range(oven_depth):
#     print(oven_radius_list[i])

dough_index = 0

for flattened_oven_index in reversed(range(oven_depth)):
    # 현재 오븐에 도우가 들어간다면
    if oven_radius_list[flattened_oven_index] >= dough_radius_list[dough_index]:
        # 다음 도우로
        dough_index = dough_index + 1
        # 그게 마지막도우였다면
        if dough_index == dough_counts:
            print(flattened_oven_index + 1)
            exit(0)

# 오븐 끝에 도달했을 경우
if flattened_oven_index == 0:
    print(0)
