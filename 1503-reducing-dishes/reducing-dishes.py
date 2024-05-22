class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        ans = 0
        for i in range(len(satisfaction)):
            Sum = 0
            for j in range(i):
                Sum+=satisfaction[j]*(j+1)
            ans = max(ans,Sum)
        for i in range(len(satisfaction)):
            Sum = 0
            count = 1
            for j in range(i,len(satisfaction)):
                Sum+=satisfaction[j]*count
                count+=1
            ans = max(ans,Sum)
        return ans