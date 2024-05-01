class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        new = []
        add = True
        for word in words:
            hasm = {}
            i=0
            while i<len(word) or i<len(word):
                if i>len(word):
                    add = False
                    break
                elif i>len(pattern):
                    add = False
                    break
                else:
                    if word[i] not in hasm.keys():
                        if pattern[i] in hasm.values():
                            add = False
                            break
                        hasm[word[i]] = pattern[i]
                    else:
                        if hasm[word[i]]!=pattern[i]:
                            add = False
                            break
                i+=1
            if add:
                new.append(word)
            add = True
        
        return new
        