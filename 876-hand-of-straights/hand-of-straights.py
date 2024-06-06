class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        else:
            c = Counter(hand)
            l = len(hand)//groupSize
            
            for i in range(l):
                temp = groupSize
                arr = []
                for each in c:
                    if (each-1 not in c or c[each-1]==0) and c[each]>0:
                        n=each
                        while n in c and temp>0:
                            if c[n]==0:
                                return False
                            else:
                                c[n]-=1
                            arr.append(n)
                            n+=1
                            temp-=1
                        if temp>1:
                            return False
                        if len(arr)!=groupSize:
                            return False
            return True
                    
