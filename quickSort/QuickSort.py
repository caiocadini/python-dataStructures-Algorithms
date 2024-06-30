def quickSort(array):
    length = len(array)
    #Condição de parada
    if length <= 1:
        return array
    
    #Definindo pivô
    pivo = array.pop()

    numeros_menores = []
    numeros_maiores = []

    for item in array:
        if item <= pivo:
            numeros_menores.append(item)
        else:
            numeros_maiores.append(item)

    return quickSort(numeros_menores) + [pivo] + quickSort(numeros_maiores)


array = [7,4,5,9,8,1]
result = quickSort(array)
print(result)
