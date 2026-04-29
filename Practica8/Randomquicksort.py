import random

def quicksort_random(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = random.choice(arr)

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort_random(left) + middle + quicksort_random(right)

ListaN = [10, 50, 23, 3, 43, 23, 29, 49, 12, 40]
print(quicksort_random(ListaN))