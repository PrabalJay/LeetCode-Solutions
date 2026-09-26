class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        a=[]
        for i,num in enumerate(nums):
            a.append([num,i])
        
        a.sort()
        i,j=0,len(nums)-1
        while i<j:
            curr=a[i][0]+a[j][0]
            if curr==target:
                return [max(a[i][1],a[j][1]),min(a[i][1],a[j][1])]
            elif curr<target:
                i+=1
            else:
                j-=1
        return []