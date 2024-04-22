class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hasm={}
        for letter in magazine:
            if letter not in hasm.keys():
                hasm[letter] = 1
            else:
                hasm[letter] +=1
        
        for letter in ransomNote:
            if letter not in hasm.keys():
                return False
            else:
                hasm[letter]-=1
                if hasm[letter]<0:
                    return False
        return True
        