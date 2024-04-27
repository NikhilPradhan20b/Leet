class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        out = []
        i=0
        for word in words:
            check = set(word)
            if x in check:
                out.append(i)
            i+=1
        return out
                