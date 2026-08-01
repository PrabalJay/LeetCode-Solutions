class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        rem={}
        count=0
        for x in time:
            r=x%60
            if r in rem:
                rem[r]=rem[r]+1
            else:
                rem[r]=1 
        if 0 in rem:
            n=rem[0]
            count=count+(n*(n-1))//2
            del rem[0]
        if 30 in rem:
            n=rem[30]
            count=count+(n*(n-1))//2
            del rem[30]
        for i in range(1,30):
            if(60-i) in rem and i in rem:
                p=rem[i]
                q=rem[60-i]
                count=count+(p*q)
        return(count)      