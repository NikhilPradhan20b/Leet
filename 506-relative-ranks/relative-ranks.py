class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        arr = [each for each in score]
        arr.sort(reverse = True)
        hasm = {}
        j=4
        for i in range(len(arr)):
            if i==0:
                hasm[arr[i]]="Gold Medal"
            elif i==1:
                hasm[arr[i]]="Silver Medal"
            elif i==2:
                hasm[arr[i]]="Bronze Medal"
            else:
                hasm[arr[i]]=str(j)
                j+=1
        for i in range(len(score)):
            score[i]=hasm[score[i]]
        return score
        