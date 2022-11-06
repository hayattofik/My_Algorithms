class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        count=0
        l=0
        j=len(nums)-1
        for i in range(len(nums)):

            if nums[l]+nums[j]==k and j>l:
                count+=1
                l+=1
                j-=1
            elif nums[l]+nums[j]>k and j>l:
                j-=1
            elif nums[l]+nums[j]<k and j>l:
                l+=1

        return count