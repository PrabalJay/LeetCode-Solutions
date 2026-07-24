class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable=0
        for current,jump in enumerate(nums):
            if reachable<current:
                return False
            reachable=max(reachable,current+jump)
        return True
        