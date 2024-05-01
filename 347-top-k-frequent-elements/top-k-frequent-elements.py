from collections import defaultdict
#just to check whether works or not// this is O(nlogn) solution
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hasm2 = defaultdict(list)
        hasm = {}
        ans = []
        for each in nums:
            if each not in hasm.keys():
                hasm[each] = 1
            else:
                hasm[each]+=1
        
        for key, value in hasm.items():
                hasm2[value].append(key)
            
        new = list(hasm2.keys())
        new.sort()
        new.reverse()
        i=0
        while k>0:
            for each in hasm2[new[i]]:
                ans.append(each)
                k-=1
            i+=1
        return ans