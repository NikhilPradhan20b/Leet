class Solution:
    def compress(self, chars: List[str]) -> int:
        i = len(chars)-1
        current = chars[i]
        count = 0
        while i>=0:
            if chars[i]==current:
                if i==0:
                    chars.pop(i)
                    count+=1
                    if count>1:
                        str_count = str(count)
                        for j in range(len(str_count)-1,-1,-1):
                            chars.append(str_count[j])
                    chars.append(current)
                    i-=1
                else:
                    chars.pop(i)
                    count+=1
                    i-=1
                
                    
            else:
                if count>1:
                    str_count = str(count)
                    for j in range(len(str_count)-1,-1,-1):
                        chars.append(str_count[j])
                chars.append(current)
                current=chars[i]
                count=0
            
        chars.reverse()
        return(len(chars))

                