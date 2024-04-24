class Solution:
    def tribonacci(self, n: int) -> int:
        a=0
        b=c=1
        if n==0:
            return a
        elif n==1:
            return b
        elif n==2:
            return c
        else:
            while n-3>=0:
                Sum = a+b+c
                a=b
                b=c
                c=Sum
                n-=1
            return Sum
        