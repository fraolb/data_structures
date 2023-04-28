def recursive_binary_search(arr, l, h, x):
    if h>= l:
        mid = l + (h - l)//2
        if (arr[mid] == x):
            return mid
        elif (arr[mid] > x):
            return recursive_binary_search(arr, l, mid-1, x)
        else:
            return recursive_binary_search(arr, mid+1, h , x)
    else: return -1

if __name__ == "__main__":
    array = [9, 8, 7, 1, 2, 3, 4, 5, 6]
    size = len(array) - 1

    value = recursive_binary_search(array, 0, size, 6)
    if (value == -1):
        print("the value of the num 4 is not stored in the array")
    else:
        print("the value of the num 4 is stored in index of ", value)