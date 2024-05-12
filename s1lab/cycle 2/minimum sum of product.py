def min_sum_of_product(arr1, arr2):
    arr1.sort()
    arr2.sort(reverse=True)  
    min_sum = sum(arr1[i] * arr2[i] for i in range(len(arr1)))
    return min_sum

arr1 = [int(x) for x in input("Enter elements of arr1 separated by space: ").split()]
arr2 = [int(x) for x in input("Enter elements of arr2 separated by space: ").split()]

if len(arr1) == len(arr2):
    min_sum = min_sum_of_product(arr1, arr2)
    print("Minimum sum of product:", min_sum)
else:
    print("Both arrays must have the same length.")
