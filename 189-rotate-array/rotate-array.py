class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = [num for num in nums]
        while k>0:
            temp = arr[-1]
            arr.pop()
            arr = [temp] + arr
            k-=1

        for i in range(len(arr)):
            nums[i] = arr[i]
            
        

        
        