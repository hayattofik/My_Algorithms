class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        
        l, r = 0, len(nums) - 1
        while len(res) != len(nums):
            res.append(nums[l])
            l += 1
            
            if l <= r:
                res.append(nums[r])
                r -= 1
        return res
        
        # for i in range(len(nums)-2,0,-1):
            

         
        #     average=(nums[i-1]+nums[i+1])/2
        #     if nums[i]== average:
        #         nums[i],nums[i+1]=nums[i+1],nums[i]
              

                    