class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @lru_cache(maxsize=None)
        def rec(i,j):
            if i==0 and j==0:
                return 1
            if i<0 or j<0:
                return 0
            left=rec(i,j-1)
            up=rec(i-1,j)
            return left+up
        return rec(m-1,n-1)
        