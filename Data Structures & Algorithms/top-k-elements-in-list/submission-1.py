class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n,0)+1
        buck = [[] for i in range(len(nums)+1)]
        for num,freq in count.items():
            buck[freq].append(num)
        res = []
        for freq in range(len(buck)-1,0,-1):
            for n in buck[freq]:
                res.append(n)
                if len(res)==k:
                    return res