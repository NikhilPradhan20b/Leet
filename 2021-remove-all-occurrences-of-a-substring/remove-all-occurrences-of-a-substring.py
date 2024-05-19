class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        # while (s.find(part)) != -1:
        #     new = [each for each in s]
        #     remove_i = s.find(part)
        #     remove_l = len(part)
        #     for i in range(remove_l):
        #         new.pop(remove_i)
        #     s = ''.join(new)
        while part in s:
            s=s.replace(part,'',1)
        return s
        