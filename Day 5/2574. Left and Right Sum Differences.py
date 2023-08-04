class Solution:
    def leftRightDifference(self, x: List[int]) -> List[int]:
        a=[]
        ls=[]
        rs=[]
        c=0
        for i in range(len(x)):
            if i==0:
                ls.append(0)
            else:
                c+=x[i-1]
                ls.append(c)
        for i in range(len(x)):
            if i==len(x)-1:
                rs.append(0)
            else:
                d=0
                d+=sum(x[i+1:len(x)])
                rs.append(d)
        for i in range(len(x)):
            e=abs(ls[i]-rs[i])
            a.append(e)
        return a
