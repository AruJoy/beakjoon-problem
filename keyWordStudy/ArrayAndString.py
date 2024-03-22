def dividingLine():
    print('=====================================================================================')

def multiDimensionalArray():
    n=5
    arr1 = [[0 for j in range(n)] for i in range(n)]
    arr2 = [[0] * n] * n
    arr3 = [[0] * n for i in range(n)]

    print(arr1)
    print(arr2)
    print(arr3)

    dividingLine()
    
    arr1[1][2] = 3
    arr2[1][2] = 3
    arr3[1][2] = 3

    print(arr1)
    print(arr2)
    print(arr3)

def oneDimensionalArray():
    n=5
    arr1 = [0 for i in range(n)]
    arr2 = [0] * n 

    print(arr1)
    print(arr2)
    
    dividingLine()
    
    arr1[2] = 3
    arr2[2] = 3
    
    print(arr1)
    print(arr2)
    
    arr3 = [[] for i in range(n)]
    arr4 =  [[]] * n
    
    arr3[2].append(3)
    arr4[2].append(3)

    print(arr3)
    print(arr4)


multiDimensionalArray()

oneDimensionalArray()