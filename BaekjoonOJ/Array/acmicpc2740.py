n, m = map(int, input().split())
arrayA = []
for i in range(n):
    arrayA.append(list(map(int, input().split())))


m, k = map(int, input().split())
arrayB = []
for i in range(m):
    arrayB.append(list(map(int, input().split())))

full_array = []

for a_row_index in range(n):
    cur_row = []
    for b_column_index in range(k):
        cur_element = 0
        for common_index in range(m):
            cur_element += arrayA[a_row_index][common_index] * arrayB[common_index][b_column_index]

        cur_row.append(cur_element)

    full_array.append(cur_row)

for i in range(n):
    for j in range(k):
        print(full_array[i][j], end=" ")
    print()


