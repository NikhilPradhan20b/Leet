class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        check = ''
        for word in words:
            check+=word[0]
        if check==s:
            return True
        else:
            return False
        