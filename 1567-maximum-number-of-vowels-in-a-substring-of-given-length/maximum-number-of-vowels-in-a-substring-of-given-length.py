class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        i, j = 0, k-1
        ans = 0
        vowels = set({'a','e','i','o','u'})
        number_of_vowels = 0
        compare = s[i:j+1]
        for letter in compare:
            if letter in vowels:
                number_of_vowels+=1
                if number_of_vowels==k:
                    return k
        ans = max(number_of_vowels,ans)
        j+=1
        i+=1
        # if i==j:
        #     j+=1
        while j < len(s):
            print(number_of_vowels) 
            if s[i-1] in vowels:
                number_of_vowels-=1
                number_of_vowels = max(0,number_of_vowels)
                print(s[i]," leaving")
            if s[j] in vowels:
                number_of_vowels+=1
                print(s[j]," entering")
            i+=1
            j+=1
            
            

            ans = max(number_of_vowels,ans)
            # print(compare)
            # print(repetition)
        return ans