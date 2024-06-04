class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        ans=0
        odd = False
        for each in c.values():
            if each%2==0:
                ans+=each
            else:
                odd = True
                ans+=each-1
        if odd:
            ans+=1
        return ans
                 