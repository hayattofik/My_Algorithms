class Solution(object):
    def Eculid_dis(self,lis):
        length=lis[0]**2 +lis[1] **2
        return length
    
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        output= sorted(points,key=self.Eculid_dis)
        finalOut=[]
        for i in range(k):
            finalOut.append(output[i])
        return finalOut