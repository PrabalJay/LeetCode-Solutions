class Solution:
    def smallestPalindrome(self, s: str) -> str:
        if len(s)==1:
            return s
        freq={}
        for ch in s:
            freq[ch]=freq.get(ch,0)+1
        left=""
        middle=""
        for ch in sorted(freq):
            left+=ch*(freq[ch]//2)
            if freq[ch]%2==1:
                middle=ch
        right=left[::-1]
        return left+middle+right