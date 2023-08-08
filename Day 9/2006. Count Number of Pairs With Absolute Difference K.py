class Solution:
    def countKDifference(self, x: List[int], k: int) -> int:
        c=0
        for i in range(len(x)):
            for j in range(len(x)):
                if(abs(x[i]-x[j])==k and i<j):
                    c+=1
        return c



# class Solution:
#     def countKDifference(self, x: List[int], k: int) -> int:
#         return sum(x.count(i+k) for i in x if i+k in x)
