import sys

A = [4,2,40,1,6,9,8, 0, -2,-1]

for i in range(len(A)):
    index_value = i
    for y in range(index_value+1, len(A)):
        if (A[index_value] > A[y]):
            index_value = y
    A[i],A[index_value] = A[index_value], A[i]

print(A)