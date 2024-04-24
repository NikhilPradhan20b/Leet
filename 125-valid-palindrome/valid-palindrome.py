class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabet = set('abcdefghijklmnopqrstuvwxyz0123456789')
        arr = s.strip().split()
        i=0
        for letter in arr:
            new = ''
            for each in letter.lower():
                if each in alphabet:
                    new+=each
            arr[i] = new
            i+=1
        check = ''.join(arr)
        alternate = "".join(reversed(check))
        if check == alternate:
            return True
        return False
        