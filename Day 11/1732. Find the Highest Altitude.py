class Solution:
    def largestAltitude(self, g: List[int]) -> int:
        s=0
        d=[]    
        d.insert(0,0)
        for i in g:
            s+=i
            d.append(s)
        return(max(d))
