class Solution:
    def minInsertions(self, s: str) -> int:
        from functools import cache
        @cache
        def dfs(left:int,right:int)->int:
            if left>=right:
                return 0
            if s[left]==s[right]:
                return dfs(left+1,right-1)
            ileft=dfs(left,right-1)
            iright=dfs(left+1,right)
            return 1+min(ileft,iright)
        return dfs(0,len(s)-1)