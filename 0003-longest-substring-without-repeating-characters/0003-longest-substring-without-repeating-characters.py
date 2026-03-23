class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        # if length of string is 1
        if n<=1:
            return n

        # add first character to set1 and ans=1
        set1=set({})
        i,j=0,1
        set1.add(s[0])
        ans=1

        # check if j is not in set1
        while j<n:
            # if j is already in set1, remove it & inc. i
            while s[j] in set1:
                set1.discard(s[i])
                i+=1
            # otherwise in set1 add j & inc. j
            set1.add(s[j])
            j+=1
            # return max. ans
            ans=max(ans,(j-i))
        
        return ans