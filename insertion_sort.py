def insertion_sort(array):
    a = len(array)

    for i in range(1, a):
        x = array[i]
        y = i-1
        while y >=0 and x < array[y]:
            array[y+1] = array[y]
            y -=1

        array[y+1] = x

A = [4,2,40,1,6,9,8, 0, -2,-1]

insertion_sort(A)
print(A)