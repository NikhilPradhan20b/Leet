class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        Sum=0
        happiness.sort(reverse = True)
        i=0
        while i<k:
            diff = max(happiness[i]-i,0)
            Sum+=diff
            # k-=1
            i+=1
        return Sum