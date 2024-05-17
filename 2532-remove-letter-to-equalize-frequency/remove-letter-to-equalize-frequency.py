class Solution:
    def equalFrequency(self, word: str) -> bool:
        def freq_max(arr):
            element = arr[0]
            count = 1
            for i in range(1,len(arr)):
                if arr[i]==element:
                    count+=1
                else:
                    count-=1
                    if count<=0:
                        element = arr[i]
                        count = 1
            return element
        # hasm = defaultdict(int)
        # for each in word:
        #     hasm[each]+=1
        # if len(hasm)==1:
        #     return True
        # check = list(hasm.values())
        # check.sort()
        # if check:
        #     done = False
        #     only_one = True
        #     for each in check:
        #         if each!=1:
        #             only_one = False
        #             break
        #     if only_one:
        #         return True
        #     else:
        #         temp = freq_max(check)
        #         for i in range(len(check)):
        #             if check[i]==temp:
        #                 continue
        #             else:
        #                 if temp>check[i] and not done:
        #                     if check[i]+1==temp:
        #                         done=True
        #                         continue
        #                     elif check[i]-1!=0:
        #                         return False
        #                     else:
        #                         done = True
        #                 elif temp+1==check[i] and not done:
        #                     done=True
        #                 else:
        #                     return False
        #     if not done:
        #         return False
        #     return True
        # else:
        #     return False
        hasm = defaultdict(int)
        for each in word:
            hasm[each]+=1
        if len(hasm)==1:
            return True
        check = list(hasm.values())
        check.sort()
        print(check)
        if len(check)==2:
            if check[0]==1:
                return True
            if check[1]-1==check[0]:
                return True
        else:
            done = False
            only_one = True
            for each in check:
                if each!=1:
                    only_one = False
                    break
            if only_one:
                return True
            else:
                temp = freq_max(check)
                for i in range(len(check)):
                    if check[i]==temp:
                        continue
                    else:
                        if temp>check[i] and not done:
                            # if check[i]-1==temp:
                            #     done=True
                            #     continue
                            if check[i]-1!=0:
                                return False
                            else:
                                done = True
                        elif temp+1==check[i] and not done:
                            done=True
                        else:
                            return False
            if not done:
                return False
            return True

            
            

            

