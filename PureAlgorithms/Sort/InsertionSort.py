def insert(target_idx, full_lists):
    for i in range(1, target_idx + 1)[::-1]:
        if full_lists[i-1] > full_lists[i]:
            full_lists[i], full_lists[i-1] = \
                full_lists[i-1], full_lists[i]
        else:
            break


def insertion_sort(full_lists):
    for i in range(1, len(full_lists)):
        insert(i, full_lists)


temp_list = [6,5,3,1,8,7,2,4]
insertion_sort(temp_list)
for i in temp_list:
    print(i, end=' ')