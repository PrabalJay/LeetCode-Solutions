class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        prefix_sum_count = Counter({0:1})
        result = 0
        current_sum = 0
        for num in nums:
            current_sum += num
            result += prefix_sum_count[current_sum - goal]
            prefix_sum_count[current_sum] += 1
        return result