class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d={} #creates a dictionary
        for index,value in enumerate(nums): #stores index and values in dict
            if value in d and index-d[value]<=k:  #checks condition
                return True
            d[value]=index  #if not satisfies, updates the index in dict
        return False