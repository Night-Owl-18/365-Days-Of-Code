class Solution:
    def countConsistentStrings(self, x: str, w: List[str]) -> int:
        c=0
        for i in range(len(w)):
            for j in range(len(w[i])):
                if w[i][j] not in x:
                    break;
            else:
                c+=1
        return c
