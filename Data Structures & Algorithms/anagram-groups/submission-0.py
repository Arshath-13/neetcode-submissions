class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res={}
        for i in strs :
            ta = "".join(sorted(i))
            if ta not in res :
                res[ta]=[]
            res[ta].append(i)
        return list(res.values())