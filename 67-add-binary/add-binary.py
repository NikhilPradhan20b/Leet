class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x = 0
        j=0
        y=0
        for i in range(len(a)-1,-1,-1):
            x+=(int(a[i])*2**j)
            j+=1

        j=0
        for i in range(len(b)-1,-1,-1):
            y+=(int(b[i])*2**j)
            j+=1

        return(str(bin(x+y))[2:])