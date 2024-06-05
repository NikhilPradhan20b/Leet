class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        c1 = Counter (words[0])
        temp =Counter (words[0])
        for word in words[1:]:
            c2 = Counter (word)
            for i in c1.keys():
                if i not in c2.keys():
                    temp.pop(i)
                else:
                    temp[i] = min(c1[i],c2[i])
            c1 = temp.copy()
        ans = []
        for each in c1:
            for i in range(c1[each]):
                ans.append(each)
        return ans