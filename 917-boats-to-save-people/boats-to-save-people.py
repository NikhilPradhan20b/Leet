class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        total = 0
        j = len(people)-1
        i=0
        while i<=j:
            diff = limit - people[j]
            total+=1
            if people[i]<=diff:
                diff -= people[i]
                i+=1
            j-=1  
        return total


        