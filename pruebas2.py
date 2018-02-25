#ordenar los números y dar el que mayor ocurrencia tenga (número, veces que sale)
def ordena(lista):
    arreglo = [0]*60
    mayor = 0 #queremos dar la mayor ocurrencia
    mayor1 = 0
    for i in range(0, len(lista)):
        arreglo[lista[i]] = arreglo[lista[i]] + 1
        if arreglo[lista[i]] > mayor:
            mayor = lista[i]
            mayor1 = arreglo[lista[i]]
    return mayor, mayor1

valores= [1, 2, 2, 3, 4, 5, 2, 3, 1, 7, 2, 2]
print(ordena(valores))