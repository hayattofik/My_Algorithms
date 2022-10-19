class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # cheLis=[]
        # start=0
        # end=0
        # count=0
        # while(start<len(fruits)):
           
        #     if fruits[start] not in cheLis and len(cheLis)<2:
        #        cheLis.append( fruits[start])
        #        start+=1
              
        #     elif fruits[start] in cheLis:
        #         cheLis.append(fruits[start])
        #         start+=1
            
        #     elif end<=len(cheLis)-1:
            
        #         cheLis.remove(cheLis[end])
        #         end+=1
        #     else:
        #         break
               
        #     count=max(count,len(cheLis))
                
            
        # return count
        dic = defaultdict(int)
        left,right,ans = 0,0,0
        while right < len(fruits):  
            if len(dic) == 2 and fruits[right] not in dic:
                dic[fruits[left]]-=1
                if dic[fruits[left]]==0:
                    del dic[fruits[left]]
                left+=1
            else:
                dic[fruits[right]]+=1
                right+=1
            ans = max(ans,right - left)
        return ans

