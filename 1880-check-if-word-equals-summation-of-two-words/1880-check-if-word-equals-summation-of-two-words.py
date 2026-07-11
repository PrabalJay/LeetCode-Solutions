class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def convert(word):
            num=""
            for ch in word:
                num+=str(ord(ch)-ord('a'))
            return int(num)
        return convert(firstWord)+convert(secondWord)==convert(targetWord)