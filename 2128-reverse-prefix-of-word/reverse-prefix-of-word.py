class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            point = word.index(ch)
            ans = word[:point+1:][::-1]
            ans+= word[point+1:]
            return ans
        else:
            return word
        