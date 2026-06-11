class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        res = 0
        
        for n in set_nums:
            if n-1 not in set_nums:
                l_seq = 1
                while n+l_seq in set_nums:
                    l_seq += 1
                res = max(res, l_seq)
        return res