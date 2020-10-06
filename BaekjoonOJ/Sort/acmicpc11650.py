point_counts = int(input())

point_lists = []
for _ in range(point_counts):
    point_lists.append(tuple(map(int, input().split())))

results = sorted(point_lists, key=lambda x:(x[0], x[1]))
for point in results:
    print(point[0], point[1])
