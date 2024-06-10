class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        new  = sorted(heights)
        ans = 0
        for i in range(len(new)):
            if new[i]!=heights[i]:
                ans+=1
        return ans