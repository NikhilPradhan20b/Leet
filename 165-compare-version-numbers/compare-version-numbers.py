class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        com1 = version1.split('.')
        com2 = version2.split('.')
        # com1 = ''
        # com2 = ''
        # for each in new1:
        #     each = int(each)
        #     com1+=str(each)
        # for each in new2:
        #     each = int(each)
        #     com2+=str(each)
        # print(com1)
        # print(com2)
        i = 0
        j = 0
        while i<len(com1) or i<len(com2):
            if i>=len(com1):
                if int(com2[j])!=0:
                    return -1
            elif j>=len(com2):
                if int(com1[j])!=0:
                    return 1
            else:
                if int(com1[i])>int(com2[j]):
                    return 1
                elif int(com1[i])<int(com2[j]):
                    return -1
            i+=1
            j+=1
        return 0    

        