class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        hasm = {}
        operations = 0
        for num in nums:
            if k-num not in hasm.keys():
                hasm[k-num] = 1
            else:
                hasm[k-num] +=1

        for num in nums:
            if num in hasm.keys() and k-num==num:
                if hasm[num]>=2:
                    hasm[num]-=2
                    operations+=1
            elif num in hasm.keys():
                if hasm[num]>=1 and hasm[k-num]>=1:
                    hasm[num]-=1
                    hasm[k-num]-=1
                    operations+=1
        return operations
        