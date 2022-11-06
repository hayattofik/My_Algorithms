class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
    
        changed.sort()
        count = Counter(changed)
        output = []
        if len(changed)%2!= 0:
            return []
        for i in changed:
            if i == 0 and count[i] >= 2:
                count[i] -= 2
                output.append(i)
            elif i > 0 and count[i] and count[i*2]:
                count[i] -= 1
                count[i*2] -= 1
                output.append(i)
        if len(output) == len(changed) // 2:
            return output
        else:
            return []