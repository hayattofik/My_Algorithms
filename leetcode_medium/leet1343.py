class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        #counter,2pointer,check with threshold,return counter
        count=0
        leftP=0
        rightP=k-1
        su=sum(arr[leftP:rightP+1])
        while(rightP<len(arr)):
          
           
            # average=sum/k
            if su>=threshold*k:
                count+=1
            su-=arr[leftP]
            leftP+=1
            rightP+=1
            if rightP<=len(arr)-1:
                su+=arr[rightP]
            else:
                break
        return count

