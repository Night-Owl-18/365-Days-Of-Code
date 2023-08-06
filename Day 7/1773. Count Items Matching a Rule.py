class Solution:
    def countMatches(self, it: List[List[str]], rk: str, rv: str) -> int:
        c = 0
        for i in it:
            if rk == 'type':
                if rv == i[0]:
                    c+= 1
            elif rk =='color':
                if rv == i[1]:
                    c+= 1
            else:
                if rv == i[2]:
                    c+= 1
        return c
