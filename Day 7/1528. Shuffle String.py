class Solution:
    def restoreString(self, s: str, ind: List[int]) -> str:
        c=""
        for i in range(len(s)):
            c+=s[ind.index(i)]
        return c
