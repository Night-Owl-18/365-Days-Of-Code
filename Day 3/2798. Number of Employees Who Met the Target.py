class Solution:
    def numberOfEmployeesWhoMetTarget(self, hr: List[int], t: int) -> int:
        c=0
        for i in range(len(hr)):
            if(hr[i]>=t):
                c+=1
        return c
