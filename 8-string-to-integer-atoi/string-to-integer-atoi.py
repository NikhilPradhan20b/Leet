class Solution:
    def myAtoi(self, s: str) -> int:
        check=set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.')
        new = s.split()
        ans = ''
        if new:
            new = new[0]
        else:
            new=""
        for i in range(len(new)):
            if new[i]=='-' and i!=0:
                break
            if new[i]=='+' and i!=0:
                break
            if new[i] in check:
                break
            ans+=new[i]
        if ans:
            if ans[0]=='+':
                ans = ans[1:]
            try:
                if int(ans)<(-2**31):
                    return (-2**31)
                if int(ans)>(2**31-1):
                    return (2**31-1)
                return int(ans)
            except:
                return 0
        return 0
        