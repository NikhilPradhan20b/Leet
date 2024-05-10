from collections import defaultdict
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        ans = []
        small = 1
        i = 0
        j = 1
        hasm=defaultdict(list)
        while i<len(arr)-1:
            if j>=len(arr):
                i+=1
                j=i+1
            else:
                # print(arr[i]/arr[j])
                # if arr[i]/arr[j] < small:
                #     small = arr[i]/arr[j]
                #     if ans:
                #         ans.pop()
                #         ans.pop()
                #     ans.append(arr[i])
                #     ans.append(arr[j])
                hasm[arr[i]/arr[j]] = [arr[i],arr[j]]
                j+=1
        x = sorted(list(hasm.keys()))
        # print(x[k-1])
        return hasm[x[k-1]]

