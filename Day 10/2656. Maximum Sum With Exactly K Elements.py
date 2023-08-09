class Solution:
    def maximizeSum(self, x: List[int], k: int) -> int:
        s=0
        for i in range(k):
            m=max(x)
            c=x.append(m+1)
            s+=m
        return s