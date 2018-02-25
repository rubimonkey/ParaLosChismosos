#Leer todos los txt de una carpeta, time stamp aaaa-mm-dd hh:mm:ss será único
import os
import glob
def leer(path):

    for filename in glob.glob(os.path.join(path, '*.txt')):
        # do your stuff
        #print(filename)
        f = open(filename, 'r')
        content = f.read()
        timestampAux = content.split("T")
        timestamp = timestampAux[1].split(":")
        print(timestamp[0]+timestamp[1]+timestamp[2])
        #Creamos un archivo auxiliar como base de datos
        file = open(path+"\\tiemposAOrdenar.txt","a")
        file.write(timestamp[0]+timestamp[1]+timestamp[2]+"#"+timestampAux[0]+"#"+filename+"*")

    file.close()

def acomodar (path):
    f = open(path, 'r')
    content = f.read()
    arreglo = content.split("*")
    #Acomodar el arreglo de acuerdo a la hr
    print(arreglo)
    ordenado = quickSort(arreglo)
    print(ordenado)

def quickSort(alist):
    #print (len(alist), "LA")
    quickSortHelper(alist,0,len(alist)-2)
    return alist

def quickSortHelper(alist,first,last):
    #print(first, last, "fistrlast")
    if first<last:

        splitpoint = partition(alist,first,last)

        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
    #print (alist, "AQUI")
    aux = alist[first].split("#")
    pivotvalue = int(aux[0]) #alist[first]
    #print(pivotvalue,"PV")
    leftmark = first+1
    rightmark = last

    done = False
    while not done:
        auxLeft = alist[leftmark].split("#")
        auxLeft = int(auxLeft[0])
        #print (auxLeft, "ALeft")
        auxRight = alist[rightmark].split("#")
        auxRight = int(auxRight[0])
        #print (auxRight, "ARight")

        while leftmark <= rightmark and auxLeft <= pivotvalue:
            leftmark = leftmark + 1

        while auxRight >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            #print(rightmark, "RM", leftmark, "LM")
            done = True

        else:
            temp = alist[leftmark]
            #print(temp, "temp")
            alist[leftmark] = alist[rightmark]
            #print (alist[leftmark], "este es mas chico")
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark


pathIn = 'C:\\Users\\Rubi\\Documents\\stan'
leer(pathIn) #Leemos los archivos y generamos un txt con la info
acomodar(pathIn +"\\tiemposAOrdenar.txt")
#buscar(pathIn+"\\lista.txt")
