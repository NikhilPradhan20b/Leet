class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasm={}
        for i in range(len(nums)):
            hasm[target-nums[i]] = i

        for j in range(len(nums)):
            if nums[j] in hasm.keys() and hasm[nums[j]]!=j:
                return [hasm[nums[j]],j] 
        