class Solution:
    def maximumNumberOfStringPairs(self, x: List[str]) -> int:
        c=0
        for i in range(len(x)):
            for j in range(i):
                if x[j]==x[i][::-1]:
                    c+=1
        return c;
