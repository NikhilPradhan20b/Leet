class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        i=0
        temp = 0
        cost = 0
        ans = 0
        for j in range(len(s)):
            cost += abs(ord(s[j])-ord(t[j]))
            temp+=1
            while cost>maxCost:
                cost-=abs(ord(s[i])-ord(t[i]))
                temp-=1
                i+=1
            ans = max(ans,temp)
        return(ans)
