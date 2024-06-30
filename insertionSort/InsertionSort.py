def insertionSort(array):
    for i in range(1, len(array)):
        current_value = array[i]
        while array[i-1] > array[i] and i > 0:
            array[i-1], array[i] = array[i], array[i-1]
            i -= 1
    return array


array = [8,5,3,1,2,4,7,9,4,423,76,7,8]

result = insertionSort(array)

print(result)
