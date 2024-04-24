class Solution:
    def countAsterisks(self, s: str) -> int:
        count = 0
        inside = False
        for value in s:
            if not inside:
                if value=='*':
                    count+=1
                elif value =='|':
                    if inside:
                        inside = False
                    else:
                        inside = True
            else:
                if value =='|':
                    if inside:
                        inside = False
                    else:
                        inside = True
            
        return count
            
            
        