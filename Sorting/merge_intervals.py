class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merge=[]
        flag=0
        # for i in range(len(intervals)-1):
        #     for j in range(len(intervals)-1-i):
        #         if intervals[j][0]>intervals[j+1][0]:
        #             intervals[j],intervals[j+1]=intervals[j+1],intervals[j]
        #             flag=1
        #     if flag==0:
        #         break
        intervals.sort()
        
            
        for interval in intervals:
            if merge and (merge[-1][1] >= interval[0]):
                merge[-1][1]=max(interval[1],merge[-1][1])
            else:
                merge.append(interval)