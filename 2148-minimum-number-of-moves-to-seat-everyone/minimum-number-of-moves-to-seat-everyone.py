class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        ans = 0
        for i in range(len(students)):
                while students[i]!=seats[i]:
                    ans+=1
                    if students[i]<seats[i]:
                        students[i]+=1
                    else:
                        students[i]-=1 
        return ans