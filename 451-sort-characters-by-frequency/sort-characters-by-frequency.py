from collections import defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        hasm = defaultdict(int)
        hasm2=defaultdict(list)
        ans=''
        for each in s:
            hasm[each]+=1
        print(hasm)
        for key,value in hasm.items():
            hasm2[value].append(key)

        new = list(hasm2.keys())
        new.sort()
        for i in range(len(new)-1,-1,-1):
            for each in hasm2[new[i]]:
                for j in range(new[i]):
                    ans+=each
        
        return ans