class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = [each for each in nums]
        arr.sort()
        hasm={}
        i=0
        for each in arr:
            if each not in hasm.keys():
                hasm[each]=i
                i+=1
            else:
                i+=1
        for i in range(len(nums)):
            nums[i] = hasm[nums[i]]
        return nums

            

