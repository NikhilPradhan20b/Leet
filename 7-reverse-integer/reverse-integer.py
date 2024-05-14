class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = -1*x
            str_x = str(x)
            str_x = str(x)[::-1]
            new_x = int(str_x)*-1
            if new_x < (-2**31):
                return 0
            else:
                return new_x
        else:
            str_x = str(x)
            str_x = str(x)[::-1]
            new_x = int(str_x)
            if new_x > (2**31-1):
                return 0
            else:
                return new_x 
