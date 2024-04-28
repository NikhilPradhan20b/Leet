class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set('AEIOUaeiou')
        new = []
        for each in s:
            if each in vowels:
                new.append(ord(each))
        new.sort()
        ans = ''
        i = 0
        for each in s:
            if each in vowels:
                ans+=chr(new[i])
                i+=1
            else:
                ans+=each
        return ans

        