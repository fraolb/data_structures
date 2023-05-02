def sort(arr, size):
    low = 0
    high = size-1
    mid = 0

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low = low + 1
            mid = mid + 1
        elif arr[mid] == 1:
            mid = mid + 1
        else:
            arr[high], arr[mid] = arr[mid], arr[high]
            high = high -1
    return arr


array = [2, 1, 0, 2, 2, 0, 1, 2]
length = len(array)

data = sort(array, length)

print(data)
