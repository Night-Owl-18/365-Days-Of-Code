class Solution:
    def smallerNumbersThanCurrent(self, x: List[int]) -> List[int]:
        a=[]  
        for i in range(len(x)):
            c=0
            for j in range(len(x)):
                if j!=i and x[j]<x[i]:
                    c+=1
            a.append(c)
        return a
