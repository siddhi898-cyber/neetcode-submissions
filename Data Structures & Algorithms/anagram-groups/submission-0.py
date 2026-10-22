class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups={}
        for i in strs:
            k="".join(sorted(i))
            if k not in groups:
                groups[k]=[]
            groups[k].append(i)
        return list(groups.values())

        