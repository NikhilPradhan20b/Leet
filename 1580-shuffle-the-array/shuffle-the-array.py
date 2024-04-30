class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i = 0
        j = n
        arr = [0] * len(nums)
        k=0
        while i<n:
            arr[k] = nums[i]
            k+=1
            arr[k] = nums[j]
            k+=1
            i+=1
            j+=1
        return arr
        