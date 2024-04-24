class Solution:
    def countAsterisks(self, s: str) -> int:
        count = 0
        inside = False
        for value in s:
            if not inside:
                if value=='*':
                    count+=1
                elif value =='|':
                    inside = not inside
            else:
                if value =='|':
                    inside = not inside
            
        return count
            
            
        