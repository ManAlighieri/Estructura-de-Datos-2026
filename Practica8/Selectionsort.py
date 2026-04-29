ListaN = [10, 50, 23, 3, 43, 23, 29, 49, 12, 40]

def Selectionsort(A):
    n = len(A)
    for i in  range(n-1):
        min_index = i
        for j in range(i+1, n):
            if A[j] < A[min_index]:
                min_index = j
        if min_index != i:
            A[i], A[min_index] = A[min_index], A[i]

Selectionsort(ListaN)
print(ListaN)
    