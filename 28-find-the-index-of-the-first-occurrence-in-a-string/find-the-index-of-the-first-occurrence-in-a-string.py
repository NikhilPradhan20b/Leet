class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i=0
        j=0
        s = 0
        while j<len(haystack):
            if haystack[j]==needle[s]:
                print(haystack[i:j+1])
                j+=1
                s+=1
                if s==len(needle):
                    return i
            else:
                i+=1
                j=i
                s=0
        return -1
        