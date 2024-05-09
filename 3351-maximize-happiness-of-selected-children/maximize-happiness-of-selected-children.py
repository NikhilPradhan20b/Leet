class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        Sum=0
        happiness.sort(reverse = True)
        # print(happiness)
        i=0
        while k>0:
            # if i==0:
            #     Sum+=happiness[i]
            diff = max(happiness[i]-i,0)
            Sum+=diff
            k-=1
            i+=1
        return Sum