class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ''
        for digit in digits:
            string+=str(digit)
        
        new = int(string)+1

        return [int(digit) for digit in str(new)]