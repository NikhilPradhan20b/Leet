class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        ans = 0

        n = len(garbage)

        m,p,g = False,False,False
        for i in range(n-1,-1,-1):
            if not g and "G" in garbage[i]:
                g=True
                ans+=sum(travel[:i])
            if not m and "M" in garbage[i]:
                m=True
                ans+=sum(travel[:i])
            if not p and "P" in garbage[i]:
                p=True
                ans+=sum(travel[:i])
            if all([m,p,g]):
                break

        return len("".join(garbage))+ans
        # def find_sum(garbage,total=0):
        #     for i in range(len(garbage)):
        #         temp = garbage[i].count('G')
        #         if temp>0:
        #             total += temp
        #         temp = garbage[i].count('P')
        #         if temp>0:
        #             total += temp
        #         temp = garbage[i].count('M')
        #         if temp>0:
        #             total += temp
        #     return total
            
        # def find(garbae,s):
        #     for j in range(len(garbage)-1,0,-1):
        #         if s in garbage[j]:
        #             return j
        #     return 0

        # def cal_sum(travel,distance):
        #     total = 0
        #     for i in range(distance):
        #         total+=travel[i]
        #     return total
            
            
        # g_len,p_len,m_len =find(garbage,'G'),find(garbage,'P'),find(garbage,'M')

        # total = find_sum(garbage)+cal_sum(travel,g_len)+cal_sum(travel,p_len)+cal_sum(travel,m_len)


        # return (total)