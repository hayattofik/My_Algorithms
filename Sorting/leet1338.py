class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        if len(set(arr))==1:
            return 1
        half=len(arr)/2
        count=0
        nuMap={}
        for i in range(len(arr)):
            if arr[i] in nuMap:
               nuMap[arr[i]]+=1
            else:
               nuMap[arr[i]]=1

        values=list(nuMap.values())
       
        values.sort()
        values.reverse()
        tmp=0
        i=0
        while(True):
           
            if tmp>=len(arr)/2:
                break
            else:
                tmp+=values[i]
                i+=1
                count+=1
        return count

