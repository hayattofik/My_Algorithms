class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mult=1
        output=[]
        for i in range(len(nums)):
            mult*=nums[i]
            output.append(mult)
        mult=1
        for j in range(len(nums)-1,0,-1):
           
            output[j]=output[j-1] * mult
            mult*=nums[j]
        output[0]=mult
        return output
