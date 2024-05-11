class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        count = 0
        check1 = set()
        check2 = set()
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                count+=1
                check1.add(s1[i])
                check2.add(s2[i])
        if count==0:
            return True
        elif count==2 and check1==check2:
            return True
        return False

        