class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new = s.split(' ')
        i = len(new)-1
        while i>=0:
            if new[i]!='':
                break
            i-=1
        
        return len(new[i])
        