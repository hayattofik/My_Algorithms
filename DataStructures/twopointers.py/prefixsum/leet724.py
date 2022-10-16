class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalsum=sum(nums)
        leftmove=0
        for i in range(len(nums)):
            rightSum=totalsum-nums[i]-leftmove
            if leftmove==rightSum:
                return i
            leftmove+=nums[i]
        return -1