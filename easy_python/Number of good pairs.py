class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if( nums[i]==nums[j] and i<j):
                    pairs.append((i,j))
                    
        return len(pairs)
                    
        