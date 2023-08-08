class Solution:
    def arithmeticTriplets(self, x: List[int], d: int) -> int:
        c=0
        for i in x:
            if i+d in x and i+2*d in x: c+=1
        return c
