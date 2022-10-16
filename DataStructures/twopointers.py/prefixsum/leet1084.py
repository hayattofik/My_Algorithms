class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        pre=[]
        sum=0
        for i in chalk:
            sum+=i
            pre.append(sum)
        k=k%sum
        for j,ele in enumerate(pre):
            if ele > k:
                return j
    
       
        
        # while(k>=0):
        #     for i,ele in enumerate(chalk):
                
        #         if ele <=k:
        #             k-=ele
        #         else:
        #             return i
        