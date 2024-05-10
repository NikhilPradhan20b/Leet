from collections import defaultdict
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        i = 0
        j = 1
        hasm=defaultdict(list)
        while i<len(arr)-1:
            if j>=len(arr):
                i+=1
                j=i+1
            else:
                hasm[arr[i]/arr[j]] = [arr[i],arr[j]]
                j+=1
        x = sorted(list(hasm.keys()))
        return hasm[x[k-1]]

