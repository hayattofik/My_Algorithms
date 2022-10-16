class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #swap when I get 0
        # for i in range(len(nums)-1):
        #     flag=0
        #     for j in range(len(nums)-1-i):
        #         if nums[j]==0:
        #             nums[j],nums[j+1]=nums[j+1],nums[j]
        #             flag=1
        #     if flag==0:
        #         break

        # return nums
        
        # #swap with end if it is 0 else keep moving
        # #cons poin
        # for j in range(len(nums)-1):
        #     for i in range(len(nums)-1):
        #         if nums[i]==0:
        #             tmp=nums[i]
        #             nums.remove(nums[i])
        #             nums.append(tmp)
        # return nums
        lp=0
        for i in range(len(nums)):
            if nums[i]==0:
                continue
            else:
                nums[lp],nums[i]=nums[i],nums[lp]
                lp+=1
        return nums
      