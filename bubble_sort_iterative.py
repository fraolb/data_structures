def sort(arr):
    x = len(arr)

    for a in range(x):
        for b in range(0, x-a-1):
            if arr[b] > arr[b+1]:
                arr[b], arr[b+1] = arr[b+1], arr[b]

    return arr


array = [5, 1, 4, 2, 8]
c = sort(array)

print(c)