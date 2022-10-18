class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score=0
        maxScore=0
        tokens.sort()

        maX=len(tokens)-1
        miN=0
        while(miN<=maX):
            if power>=tokens[miN]:
                power-=tokens[miN]
                score+=1
                miN+=1
                maxScore=max(score,maxScore)
            elif score >=1 and len(tokens)>2:
                power+=tokens[maX]
                maX-=1
                
                score-=1
            else:
                break
           
        return maxScore
    
