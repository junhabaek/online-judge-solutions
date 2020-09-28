def quick_sort(arr, low_idx, high_idx):
    if low_idx < high_idx:
        pivot_value = arr[high_idx]
        left_idx = low_idx

        for right_idx in range(low_idx, high_idx):
            if arr[right_idx] < pivot_value:
                arr[left_idx], arr[right_idx] = arr[right_idx], arr[left_idx]
                left_idx = left_idx + 1
        arr[left_idx], arr[high_idx] = arr[high_idx], arr[left_idx]

        quick_sort(arr, low_idx, left_idx - 1)
        quick_sort(arr, left_idx + 1, high_idx)


# sample_list = [2,8,7,1,3,5,6,4]
sample_list = [26,5,37,1,61,11,59,15,48,19]
quick_sort(sample_list, 0, len(sample_list))
for i in sample_list:
    print(i)