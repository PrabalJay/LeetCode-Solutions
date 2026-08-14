class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        x=set()
        res=0
        i=0
        n=len(s)
        for j in range(n):
            while s[j] in x:
                x.remove(s[i])
                i+=1
            x.add(s[j])
            res=max(res,j-i+1)
        return res