class Solution:
    def buildArray(self, x: List[int]) -> List[int]:
        y=[]
        for i in range(len(x)):
            y.append(x[x[i]])
        return y
