class Solution:
    def differenceOfSum(self, x: List[int]) -> int:
        s=0
        for i in x:
            j=i
            r=i%10
            s+=r
            i//=10
            if(j>=10):
                for j in range(i):
                    r=i%10
                    s+=r
                    i//=10
        return sum(x)-s

