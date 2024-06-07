class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        arr = sentence.split()
        for i in range(len(arr)):
            l=float('inf')
            for each in dictionary: 
                n = len(each)
                if n<l:
                    word = arr[i][:n]
                    if each==word:
                        arr[i]=each
                        l=n
        return " ".join(arr)