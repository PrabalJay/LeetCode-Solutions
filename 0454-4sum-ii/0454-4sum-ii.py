class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # # TLE
        # ans=0
        # for i in range(len(nums1)):
        #         for j in range(len(nums2)):
        #             for k in range(len(nums3)):
        #                 for l in range(len(nums4)): 
        #                     if nums1[i]+nums2[j]+nums3[k]+nums4[l]==0:
        #                         ans+=1
        # return ans

        mp={}
        for a in nums1:
            for b in nums2:
                s=a+b
                mp[s]=mp.get(s,0)+1
                
        ans=0
        for c in nums3:
            for d in nums4:
                target=-(c+d)
                if target in mp:
                    ans+=mp[target]
        return ans