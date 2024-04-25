class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        compare = set("!?',;. ")
        new = paragraph.lower().strip().split(',')
        test = ' '.join(new)
        new = test.strip().split()
        hasm={}
        most = 0
        current = ''
        for i in range(len(new)):
            out = ''
            for each in new[i]:
                if each not in compare:
                    out+=each   
                new[i] = out
        for each in new:
            if each not in hasm.keys():
                hasm[each] = 1
            else:
                hasm[each] +=1
        for key,value in hasm.items():
            if key not in banned:
                if value>most:
                    current = key
                    most = value
        return current
        