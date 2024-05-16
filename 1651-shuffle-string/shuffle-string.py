class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        arr = [0]*(len(indices))
        i=0
        for each in indices:
            arr[each] = s[i]
            # print(arr[i])
            i+=1
            
        return ''.join(arr)
