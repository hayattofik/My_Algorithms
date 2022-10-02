def merge(a,b):
    finalArr=[]
    while(a and b):
        if a[0] > b[0]:
            finalArr.append(b[0])
            b.remove(b[0])
        else:
            finalArr.append(a[0])
            a.remove(a[0])
    while(a):
        finalArr.append(a[0])
        a.remove(a[0])
    while(b):
        finalArr.append(b[0])
        b.remove(b[0])
    return finalArr

def mergeSort(arr):
    if(len(arr)==1):
        return arr
    arrOne=arr[0:int(len(arr)/2)]
    arrTwo=arr[int(len(arr)/2):len(arr)]
    arrOne=mergeSort(arrOne)
    arrTwo=mergeSort(arrTwo)
    return merge(arrOne,arrTwo)
lis=[3,5,2,8,9,0,1]
print(mergeSort(lis))
