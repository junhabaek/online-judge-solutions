def merge(full_lists, start, end):
    middle = int((start + end) / 2)
    idx1 = start
    idx2 = middle+1

    temp_lists = []

    while idx1 <= middle and idx2 <= end:
        if full_lists[idx1] <= full_lists[idx2]:
            temp_lists.append(full_lists[idx1])
            idx1 = idx1+1
        else:
            temp_lists.append(full_lists[idx2])
            idx2 = idx2+1

    while idx1 <= middle:
        temp_lists.append(full_lists[idx1])
        idx1 = idx1+1

    while idx2 <= end:
        temp_lists.append(full_lists[idx2])
        idx2 = idx2+1

    for i in range(end-start+1):
        full_lists[start + i] = temp_lists[i]


def merge_sort(full_lists, start, end):
    if start == end:
        return

    middle = int((start+end)/2)
    merge_sort(full_lists, start, middle)
    merge_sort(full_lists, middle+1, end)

    merge(full_lists, start, end)


target_list = [6,5,3,1,8,7,2,4]
# target_list = [3,2,4]
merge_sort(target_list, 0, len(target_list)-1)

for i in target_list:
    print(i)
