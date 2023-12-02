def selection_sort1(array1):
    n = len(array1)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if array1[j] < array1[min_index]:
                min_index = j

        array1[i], array1[min_index] = array1[min_index], array1[i]

def selection_sort2(array2):
    n = len(array2)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if array2[j] > array2[min_index]:
                min_index = j

        array2[i], array2[min_index] = array2[min_index], array2[i]

def min_sum_of_product(array1, array2):
    selection_sort1(array1)
    selection_sort2(array2)

    min_sum = 0
    for i in range(len(array1)):
        min_sum += array1[i] * array2[i]

    return min_sum

array1 = [2, 3, 1, 4, 5, 7, 23]
array2 = [4, 2, 3, 1, 6, 78, 22]

result = min_sum_of_product(array1, array2)
print(f"Minimum sum of product: {result}")
