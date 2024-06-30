def mergeSort(array):
    if len(array) <= 1:
        return array
    # Divindindo array no meio
    left_array = array[:len(array)//2] 
    right_array = array[len(array)//2:]

    #Dividir o array recursivamente
    left_array = mergeSort(left_array)
    right_array = mergeSort(right_array)

    sorted_array = []
    j = k = 0
    #Ordenando por comparação entre partes menores
    while k < len(left_array) and j < len(right_array):
        if(left_array[k] < right_array[j]):
            sorted_array.append(left_array[k])
            k += 1
        else:
            sorted_array.append(right_array[j])
            j += 1
    # Colocar elementos restantes em cada array
    while k < len(left_array):
        sorted_array.append(left_array[k])
        k += 1
    
    while j < len(right_array):
        sorted_array.append(right_array[j])
        j += 1
    
    return sorted_array
        

arr = [38, 27, 43, 3, 9, 82, 10]
print("Original Array:", arr)

result = mergeSort(arr)
print("Sorted Array:", result)
    