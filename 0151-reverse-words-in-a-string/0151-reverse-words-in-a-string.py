class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip().split()[::-1]     # remove spaces, splits into list, reverses it
        s=" ".join(s)                 # joins the reversed list with spaces
        return s