def insertion_sort(arr):
    for i in range(1,len(arr)):
        temp=arr[i]
        j=i-1
        while(j>=0 and arr[j]>temp):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=temp

    return arr
lis=[3,5,2,8,9,0,1]
print(insertion_sort(lis))

