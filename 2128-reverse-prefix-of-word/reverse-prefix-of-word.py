class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        point = word.index(ch)
        ans = word[:point+1:][::-1] + word[point+1:]
        return ans
        