class Solution:
    import math
    def climbStairs(self, n: int) -> int:
        ways = 0
        digits = n-1
        n_way=1
        if digits>=0:
            ways+=1
        while n_way<=digits:
            ways+=math.comb(digits,n_way)
            n_way+=1
            digits-=1
        return ways
            
        


        