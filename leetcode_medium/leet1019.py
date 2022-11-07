class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        ans=[0]*len(arr)
        indexMap=[(num,idx) for idx,num in enumerate(arr)]
        stack=[]
        for idx,num in enumerate(arr):
            while stack and stack[-1][0]<num:
                ans[stack.pop()[1]]=num
            stack.append((num,idx))
        return ans
