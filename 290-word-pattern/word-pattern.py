class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        i=0
        hasm={}
        s  = s.split()
        while i<len(s) or i<len(pattern):
            if i>=len(pattern):
                return False
            if i>=len(s):
                return False
            if pattern[i] not in hasm.keys():
                if s[i] not in set(hasm.values()):
                    hasm[pattern[i]] = s[i]
                else:
                    return False
            else:
                if hasm[pattern[i]]!=s[i]:
                    return False
                # elif s[i] in set(hasm.values()):
                #     return False
            i+=1
        return True
        