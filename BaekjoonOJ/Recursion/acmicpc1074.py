N, r, c = map(int, input().split())

cur_n = N
middle = 2**(N-1)
area = middle * middle
target_x, target_y = r, c

order = 0

while cur_n >= 1:
    if target_x >= middle:
        if target_y >= middle:
            order += area * 3
            target_y -= middle
        else:
            order += area * 2
        target_x -= middle
    else:
        if target_y >= middle:
            order += area
            target_y -= middle

    cur_n -= 1
    middle //= 2
    area //= 4

print(order)
