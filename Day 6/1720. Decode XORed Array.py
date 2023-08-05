class Solution:
    def decode(self, e: List[int], f: int) -> List[int]:
        d=[]
        d.append(f)
        for i in range(1,len(e)+1):
            d.append(d[-1] ^ e[i-1])
        return d
