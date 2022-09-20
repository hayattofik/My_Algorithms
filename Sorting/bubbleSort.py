def BubbleSort(lis):
    flag=0
    for i in range(len(lis)-1):
        for j in range(len(lis)-1-i):
            if lis[j]>lis[j+1]:
                lis[j],lis[j+1]=lis[j+1],lis[j]
                flag=1
        if flag==0:
            break
    return lis
lis=[3,5,2,8,9,0,1]
print(BubbleSort(lis))