class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        count = 0
        for each in sentences:
            new = each.split()
            count = max(count,len(new))
        return count
        