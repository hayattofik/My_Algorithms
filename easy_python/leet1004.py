class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start=0
        end=0
        while(start<len(nums)):
            if nums[start]==0:
                k-=1
            if k<0:
                if nums[end]==0:
                    k+=1
                end+=1
            start+=1
        return (start-end)