class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        memo={}
        l,r,max_length=0,0,0
        while r<len(s):
            ch=s[r]
            if ch in memo and memo[ch]>=l:
                l=memo[ch]+1
            memo[ch]=r
            max_length=max(max_length,r-l+1)
            r+=1
        return max_length