ListaN = [10, 50, 23, 3, 43, 23, 29, 49, 12, 40]

def bubblesort(ListaN):
    n = len(ListaN)
    for i in range (n-1):
        intercambiado = False
        for j in range (n-i-1):
            if ListaN[j] > ListaN[j+1]:
                ListaN[j], ListaN[j+1] = ListaN[j+1], ListaN[j]
                intercambiado = True
        if not intercambiado:
            break

bubblesort(ListaN)
print(ListaN)


