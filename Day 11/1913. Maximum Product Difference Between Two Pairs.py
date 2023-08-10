class Solution:
    def maxProductDifference(self, x: List[int]) -> int:
        x.sort()
        return((max(x)*x[-2])-(min(x)*x[1]))
