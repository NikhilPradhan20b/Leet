class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        arr = [a,b,c]
        arr.sort()
        a = arr[0]
        b = arr[1]
        c = arr[2]
        ans = 0
        while a!=0:
            if c>b:
                c-=1
            else:
                b-=1
            ans+=1
            a-=1
        ans+=b
        return ans

        



            