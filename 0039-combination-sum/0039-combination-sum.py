class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        path=[]
        def back(idx,rem):
            if rem==0:
                res.append(path[:])
                return
            if rem<0:
                return
            for i in range(idx,len(candidates)): 
                path.append(candidates[i])
                back(i,rem-candidates[i])
                path.pop()
        back(0,target)
        return res