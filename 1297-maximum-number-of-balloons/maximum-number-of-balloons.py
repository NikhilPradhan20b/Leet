class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hasm = {}
        count = 0
        word = set('balloon')
        for letter in text:
            if letter not in hasm.keys() and letter in word:
                hasm[letter] = 1
            elif letter in word:
                hasm[letter]+=1
        
        
        
        
        if len(hasm.values()) < 5:
            return count
        else:
            hasm['l'],hasm['o'] = hasm['l']//2,hasm['o']//2
            return min(hasm.values())
        
            


        