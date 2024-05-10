class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        number = len(piles)//3
        piles.sort(reverse = True)
        Sum = 0
        j=1
        # print(number)
        for i in range(number):
            Sum+=piles[j]
            j+=2
        return Sum
        