import os
import glob

def read(path):

    for filename in glob.glob(os.path.join(path, '*.txt')):
        # do your stuff
        #print(filename)
        f = open(filename, 'r')
        content = f.read()
        timestampAux = content.split("T")
        timestamp1 = timestampAux[0].split("-")
        timestamp2 = timestampAux[1].split(":")
        print(timestamp1[0]+timestamp1[1]+timestamp1[2]+timestamp2[0]+timestamp2[1]+timestamp2[2])
        #Creamos un archivo auxiliar como base de datos
        file = open(path+"\\tiemposAOrdenar.txt","a")
        file.write(timestamp1[0]+timestamp1[1]+timestamp1[2]+timestamp2[0]+timestamp2[1]+timestamp2[2]+"#"+filename+"*")

    file.close()


def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-2)

def quickSortHelper(alist,first,last):
    #print(first, last, "fistrlast")
    if first<last:

        splitpoint = partition(alist,first,last)

        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)
    #print(alist, "Alist")


def partition(alist,first,last):
    aux = alist[first].split("#")
    pivotvalue = int(aux[0])
    print(pivotvalue, "PV")

    leftmark = first+1
    rightmark = last

    done = False
    while not done:

        auxLeft = alist[leftmark].split("#")
        auxLeft = int(auxLeft[0])
        auxRight = alist[rightmark].split("#")
        auxRight = int(auxRight[0])
        print(auxLeft, "AL", auxRight, "AR")

        while leftmark <= rightmark and auxLeft <= pivotvalue:
            leftmark = leftmark + 1

        while auxRight >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp


    return rightmark

def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False

    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            print(alist)
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1

    return found

pathIn = 'C:\\Users\\Rubi\\Documents\\stan'
#read(pathIn) #comentas esta línea cuando el archivo txt ya existe

f = open(pathIn+"\\tiemposAOrdenar.txt", 'r')
content = f.read()
arreglo = content.split("*")
#Acomodar el arreglo de acuerdo a la hr
print(arreglo)
quickSort(arreglo)
print(arreglo)
#alist = [20341219920427,20341219920426,20341219920423,17203412199204,77203412199204,32034121992071,2034121994274,55203412199207]
#quickSort(alist)
#print(alist)
#testlist = arreglo
#print(binarySearch(testlist, 3))
#print(binarySearch(testlist, 16))