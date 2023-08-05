class Solution:
    def createTargetArray(self, n: List[int], ix: List[int]) -> List[int]:
        tr=[]
        for i in range(len(n)):
            tr.insert(ix[i],n[i])
        return tr
