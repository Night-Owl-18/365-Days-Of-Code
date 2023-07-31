class Solution:
    def maximumWealth(self, a: List[List[int]]) -> int:
        c=[]
        for i in range(len(a)):
            t=0
            for j in range(len(a[i])):
                t+=a[i][j]
            c.append(t)
        return max(c)
