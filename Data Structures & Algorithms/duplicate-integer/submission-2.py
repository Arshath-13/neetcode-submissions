class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list_len = len(nums)
        s = set(nums)
        set_len = len(s)
        if(list_len == set_len):
            return False
        else:
            return True    