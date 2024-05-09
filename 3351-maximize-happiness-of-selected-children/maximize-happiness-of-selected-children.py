class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        Sum=0
        happiness.sort(reverse = True)
        # print(happiness)
        i=0
        j=0
        while k>0:
            if i==0:
                Sum+=happiness[i]
            else:
                diff = max(happiness[i]-j,0)
                Sum+=diff
            k-=1
            j+=1
            i+=1
        return Sum