class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        # queryIP = "172.16.254..1"
        check = set('abcdefABCDEF')
        no_check = set('0123456789')
        new = []
        if '.' in queryIP:
            new = queryIP.split('.')
            countv4 = 0
            for each in new:
                countv4+=1
                count = 0
                temp = ''
                if countv4>4:
                    return 'Neither'
                for x in each:
                    if x in no_check:
                        temp+=x
                    else:
                        return 'Neither'
                if len(temp)==0 or int(temp)>255 :
                    return 'Neither'
                elif len(str(int(temp)))!=len(temp):
                    return 'Neither'
            if countv4<4:
                return 'Neither'
            return 'IPv4'
        
        elif ':' in queryIP:
            new = queryIP.split(':')
            countv6 = 0
            for each in new:
                countv6+=1
                count = 0
                if countv6>=9:
                    return 'Neither'
                for x in each:
                    count+=1
                    if count>=5:
                        return 'Neither'
                    if x not in check and x not in no_check:
                        return 'Neither'
                if len(each)==0:
                    return 'Neither'           
            return 'IPv6'
        
        # if countv6<8:
        #         return 'Neither'
        return 'Neither'

        