class Solution:
    def rob(self, nums: list[int]) -> int:
        yes, no = 0, 0        
        for num in nums:
            yes, no = num + no, max(yes, no)
        return max(yes, no)