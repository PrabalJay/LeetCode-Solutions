class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # ans=0
        # for i in range(limit+1):
        #     for j in range(limit+1):
        #         for k in range(limit+1):
        #             if i+j+k==n:
        #                 ans+=1
        # return ans

# --------------------------------------------------
        # ans=0
        # for i in range(limit+1):
        #     for j in range(limit+1):
        #         k=n-i-j
        #         if 0<=k<=limit:
        #             ans+=1
        # return ans

# ----------------------------------------------------
        ans=0
        for i in range(limit+1):
            left=max(0,n-i-limit)
            right=min(limit,n-i)
            if left<=right:
                ans+=right-left+1
        return ans