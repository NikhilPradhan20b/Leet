class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hasm = {}
        for each in arr:
            if each not in hasm.keys():
                hasm[each] = 1
            else:
                hasm[each]+=1
        hasm2 = {}
        for key,value in hasm.items():
            hasm2[value] = key
        
        if len(hasm2.keys())==len(hasm.keys()):
            return True
        return False
        