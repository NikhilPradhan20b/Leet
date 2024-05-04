class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        total = 0
        j = len(people)-1
        i=0
        print(people)
        while i<=j:
            diff = limit - people[j]
            total+=1
            # while diff>0:
            if people[i]<=diff:
                diff -= people[i]
                i+=1
            # elif i==j:
            #     diff = 0
            # else:
            #     diff = 0
            j-=1  
        return total


        