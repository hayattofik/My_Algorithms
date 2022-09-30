class Solution:
    def sortSentence(self, s: str) -> str:
        sendic={}
        a=s.split()
        sortedSent=""
        for i in range(len(a)):
            word=a[i][0:-1]
            index=a[i][-1]
            sendic[index]=word
        for j in range(1,len(a)+1):

            sortedSent+=sendic[str(j)]
            if j==len(a):
                break
            sortedSent+=" "
        return sortedSent