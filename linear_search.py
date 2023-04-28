def iterative_search(arr, x):
    a = len(arr)
    for i in range(0, a):
        if (arr[i] == x):
            return i
    return -1

def recursive_search(arr, x , size):
    if (size == 0):
        return -1
    elif(arr[size] == x):
        return size
    else:
        return recursive_search(arr,x, size-1)

if __name__ == "__main__":
    array = [9, 8, 7, 1, 2, 3, 4, 5, 6]
    size = len(array) -1
    #value = iterative_search(array,4)
    value = recursive_search(array, 41, size)
    if (value == -1):
        print("the value of the num 4 is not stored in the array")
    else:print("the value of the num 4 is stored in index of ", value)

