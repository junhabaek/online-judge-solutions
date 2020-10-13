n, k = map(int, input().split())

nums = list(map(int, input().split()))


def find_k(arr, start, end, _k):

    pivot = arr[start]

    left, right = start + 1, end

    while left < right:

        while left < end +1 and arr[left] < pivot:
            left += 1

        while right > start and arr[right] > pivot:
            right -= 1

        if left < right:
            arr[left], arr[right] = arr[right], arr[left]

    arr[right], arr[start] = arr[start], arr[right]

    if right == _k:
        return arr[right]
    elif right > _k:
        return find_k(arr, start, right-1, _k)
    else:
        return find_k(arr, right+1, end, _k)


print(find_k(nums, 0, len(nums)-1, k-1))
