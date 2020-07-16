oven_depth, dough_counts = map(int, input().split())
oven_radius_list = list(map(int, input().split()))
dough_radius_list = list(map(int, input().split()))

cur_depth = oven_depth
cannot_be_added = False

for cur_radius in dough_radius_list:
    if cur_depth == 0:
        cannot_be_added = True
        break
    for i in range(0, cur_depth):
        if cur_radius > oven_radius_list[i]:
            cur_depth = i
            # print(i, end=",")
            # print(cur_radius)
            break
        elif i == cur_depth-1:
            # print(i, end=",")
            # print(cur_radius)
            cur_depth = cur_depth-1


if cannot_be_added:
    print(0)
else:
    print(cur_depth)