def prefixsum(arr):
    preLis=[]
    sum=0
    for i in range(len(arr)):
        sum+=arr[i]
        preLis.append(sum)
    return preLis
a=[1,2,3,4,5,6]
print(prefixsum(a))
