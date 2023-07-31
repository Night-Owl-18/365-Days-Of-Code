class Solution:
    def mostWordsFound(self, s: List[str]) -> int:
        # for i in range(len(s)):
        #     s[i]=len(s[i].split())
        return max([len(i.split()) for i in s])