class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        maxi=0
        nums.sort()
        start=0
        end=len(nums)-1
   
        while(end>start):
            su=nums[start]+nums[end]
        
            maxi=max(maxi,su)
            start+=1
            end-=1
        return maxi
        