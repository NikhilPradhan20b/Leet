class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hasm = {}
        i=0
        while i<len(s) or i<len(t):
            if i>len(s):
                return False
            elif i>len(t):
                return False
            else:
                if s[i] not in hasm.keys():
                    if t[i] in (hasm.values()):
                        return False
                    hasm[s[i]] = t[i]
                else:
                    if hasm[s[i]]!=t[i]:
                        return False
            i+=1
        return True
        