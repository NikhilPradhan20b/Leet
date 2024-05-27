class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        i=0
        while i<len(nums) and nums[i]==0:
            i+=1
        k=1
        hasm = defaultdict(int)
        while i < len(nums):
            if nums[i]<k:
                i+=1
            else:
                hasm[k] = len(nums)-i
                k+=1
        for key,value in hasm.items():
            if key==value:
                return key
        return -1