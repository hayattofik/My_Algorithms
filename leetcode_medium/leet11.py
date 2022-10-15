class Solution:
    def maxArea(self, height: List[int]) -> int:
        # calculate the area
        # have 2 pointers
        # width=the - b/n the 2 inces
        # height = the smallest height
        # area=width*height
        # save area
        # no change on the larger height
        start=0
        end=len(height)-1
        Area=0
        currhe=0
        while(end > start):
            
            width=(end-start)
            heightStart=height[start]
            heightend=height[end]
            if heightStart < heightend:
                currhe=heightStart
               
                start+=1
            else:
                currhe=heightend
                end-=1
            AreaTmp=currhe * width
            if AreaTmp > Area:
                Area=AreaTmp
          
           
        return Area
        # Area=0
        # currhe=0
        # for i in range(len(height)):
        #     for j in range(i,len(height)):
        #         width=j-i
        #         heightStart=height[i]
        #         heightend=height[j]
        #         if heightStart < heightend:
        #             currhe=heightStart
                    
        #         else:
        #             currhe=heightend
        #         Area1=currhe*width
        #         if Area1>Area:
        #             Area=Area1
        # return Area
                    
                


                
            