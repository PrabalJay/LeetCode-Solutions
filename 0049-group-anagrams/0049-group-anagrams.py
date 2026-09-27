class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res=defaultdict(list)
        for s in strs:
            sorteds="".join(sorted(s))
            res[sorteds].append(s)
        return list(res.values())