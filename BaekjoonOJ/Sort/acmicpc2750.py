length = int(input())

target_list = [-1001]
for i in range(1, length+1):
    target = int(input())
    target_list.append(target)

    cur_place = i
    while cur_place > 0:
        if target_list[cur_place - 1] > target:
            target_list[cur_place] = target_list[cur_place - 1]
            cur_place = cur_place - 1
        else:
            break
    target_list[cur_place] = target

for i in target_list[1:]:
    print(i)
