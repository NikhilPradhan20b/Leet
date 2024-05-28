class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        i=0
        cost = 0
        ans = 0
        for j in range(len(s)):
            cost += abs(ord(s[j])-ord(t[j]))
            while cost>maxCost:
                cost-=abs(ord(s[i])-ord(t[i]))
                i+=1
            ans = max(ans,j-i+1)
        return(ans)
