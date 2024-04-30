class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans = ''
        for each in address:
            if each =='.':
                ans+='[.]'
            else:
                ans+=each
        return ans
        