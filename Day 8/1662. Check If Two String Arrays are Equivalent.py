class Solution:
    def arrayStringsAreEqual(self, w1: List[str], w2: List[str]) -> bool:
        a=""
        b=""
        for i in w1:
            a+=i
        for j in w2:
            b+=j
        if(a!=b):
            return False
        else:
            return True
