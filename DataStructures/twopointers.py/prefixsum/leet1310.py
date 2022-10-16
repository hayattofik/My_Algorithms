class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
       
        res=[]
        prefix=[0]*(len(arr)+1)
        for i in range(len(arr)):
 
            prefix[i+1]=prefix[i]^arr[i]
        
        for start,end in queries:
           st=prefix[start]
           #since it is inclusive
           en=prefix[end+1]
           temp=st^en
           res.append(temp)
            
        return res
        