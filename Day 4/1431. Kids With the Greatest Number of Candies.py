class Solution:
    def kidsWithCandies(self, c: List[int], ec: int) -> List[bool]:
        res=[]
        for i in range(len(c)):
            if c[i]+ec>=max(c):
                res+=[True]
            else:
                res+=[False]
        return res
