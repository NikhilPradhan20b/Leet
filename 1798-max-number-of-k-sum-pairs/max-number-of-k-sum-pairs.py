class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        hasm = {}
        operations = 0
        for num in nums:
            if k-num not in hasm.keys():
                hasm[k-num] = 1
            else:
                hasm[k-num] +=1
        print(hasm)

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



        # return(operations)
        # i = 0
        # operations = 0
        # delete = False
        # while i<len(nums):
        #     to_find = k-nums[i]
        #     j = i+1
        #     while j<len(nums):  
        #         if nums[j]==to_find:
        #             operations+=1
        #             nums.pop(j)
        #             nums.pop(i)
        #             delete = True
        #             break
        #         j+=1
        #     if not delete:
        #         i+=1
        #     delete=False
        # return operations
            
