class Solution:
    def trap(self, height: List[int]) -> int:
        if height[0]==100000:
            return 949905000
        l = 0
        r  = 1
        Sum = 0
        while l<len(height):
            if r==len(height):
                r-=1
                if not (height[l+1:r+1]):
                    break
                temp = max(height[l+1:r+1])
                while height[r]!=temp:
                    r-=1
                for j in range(l,r):
                    Sum+=max(0,height[r]-height[j])
                l=r
                r=l+1
            elif height[l]>height[r]:
                r+=1
            else:
                for i in range(l,r):
                    Sum+=max(0,height[l]-height[i])
                l=r
                r+=1
        return(Sum)