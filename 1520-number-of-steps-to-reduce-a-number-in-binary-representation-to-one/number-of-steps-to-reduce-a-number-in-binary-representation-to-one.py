class Solution:
    def numSteps(self, s: str) -> int:
        s= list(s)
        count = 0
        while len(s)>1:
            i=-2
            count+=1
            if s[-1]=="1":
                while abs(i)<=len(s) and s[i]=="1":
                    i-=1
                if abs(i)>len(s):
                    for j in range(1,len(s)):
                        s[j]="0"
                    s.append("0")
                else:
                    s[i]="1"
                    for j in range(len(s)-1,len(s)-abs(i),-1):
                        s[j]="0"
            else:
                s.pop()
        
        return(count)