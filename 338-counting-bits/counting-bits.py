class Solution:
    def countBits(self, n: int) -> List[int]:
        out = [0]
        count = 0
        for i in range(1,n+1):
            a = str(bin(i))[2:]
            for letter in a:
                if letter == '1':
                    count+=1
            out.append(count)
            count=0
        return out

        