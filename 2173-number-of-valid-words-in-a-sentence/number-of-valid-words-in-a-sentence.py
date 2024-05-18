class Solution:
    def countValidWords(self, sentence: str) -> int:
        sentence = sentence.split()
        check_digit = set('0123456789')
        alphabet = set('abcdefghijklmnopqrstuvwxyz')
        valid_count = 0
        for word in sentence:
            broken = False
            d_count = e_count = dot_count = c_count = 0
            for i in range(len(word)):
                if word[i]=='.':
                    dot_count+=1
                    if dot_count>1:
                        broken=True
                        break
                if word[i]=='-':
                    d_count+=1
                    if d_count>1:
                        broken=True
                        break
                if word[i]=='!':
                    e_count+=1
                    if e_count>1:
                        broken=True
                        break
                if word[i]==',':
                    c_count+=1
                    if c_count>1:
                        broken=True
                        break
                if word[i] in check_digit:
                    broken = True
                    break
                if word[i]=='!' and i!=len(word)-1:
                    broken = True
                    break
                if word[i]=='.' and i!=len(word)-1:
                    broken = True
                    break
                if word[i]==',' and i!=len(word)-1:
                    broken = True
                    break
                if word[i]=='-' and (i==0 or i==len(word)-1):
                    broken = True
                    break
                if (word[i]=='-') and (word[i-1] not in alphabet or word[i+1] not in alphabet):
                    broken = True
                    break
            if not broken:
                valid_count +=1
                # print('Valid Word: ', word)
        return valid_count
