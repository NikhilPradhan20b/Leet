class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        lsum = [0] * len(nums)
        Sum = 0
        for i in range(1,len(lsum)):
            Sum += nums[i-1]
            lsum[i] = Sum
        Sum=0
        for i in range(len(nums)-2,-1,-1):
            Sum += nums[i+1]
            # print(Sum)
            lsum[i] = abs(lsum[i]-Sum)
        return lsum