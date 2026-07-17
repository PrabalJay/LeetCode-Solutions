class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n=len(nums)
        m=len(multipliers)
        memo={}
        def solve(i,l):
            if i==m:
                return 0
            if (i,l) in memo:
                return memo[(i,l)]
            r=n-1-(i-l)
            left=multipliers[i]*nums[l]+solve(i+1,l+1)
            right=multipliers[i]*nums[r]+solve(i+1,l)
            memo[(i,l)]=max(left,right)
            return memo[(i,l)]
        return solve(0,0)