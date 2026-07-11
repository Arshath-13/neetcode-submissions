class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = []
        n = len(arr)
        for i in range(n):
            if i == n-1 :
                res.append(-1)
            else:
                res.append(max(arr[i+1:]))
        return res 
