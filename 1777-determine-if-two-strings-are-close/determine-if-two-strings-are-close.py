class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)

        for each in c1.keys():
            if each not in c2.keys():
                return(False)

        check1 = sorted(list(c1.values()))
        check2 = sorted(list(c2.values()))
        if len(check1)!=len(check2):
            return False
        for i in range(len(check1)):
            if check1[i]!=check2[i]:
                return False

        if len(word1)!=len(word2):
            return(False)
        else:
            return True