class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max_val=min_val=nums[0]
        for n in nums[1:]:
            temp_max=max(n,max_val*n,min_val*n)
            min_val=min(n,max_val*n,min_val*n)
            max_val=temp_max
            res=max(res,max_val)
        return res