def mergeSort(array):
    if len(array) > 1:
        # Divindindo array no meio
        left_array = array[:len(array)//2] 
        right_array = array[len(array)//2:]

        #Dividir o array recursivamente
        mergeSort(left_array)
        mergeSort(right_array)

        i = j = k = 0
        #Ordenando por comparação entre partes menores
        while k < len(left_array) and j < len(right_array):
            if(left_array[k] < right_array[j]):
                array[i] = left_array[k]
                k += 1
            else:
                array[i] = right_array[j]
                j += 1

            i += 1
        # Colocar elementos restantes em cada array
        while k < len(left_array):
            array[i] = left_array[k]
            k += 1
            i += 1
        
        while j < len(right_array):
            array[i] = right_array[j]
            j += 1
            i += 1
        

arr = [38, 27, 43, 3, 9, 82, 10]
print("Original Array:", arr)

mergeSort(arr)
print("Sorted Array:", arr)
    