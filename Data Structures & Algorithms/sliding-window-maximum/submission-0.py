class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        win = []
        max_elements = []
        left = 0
        right = k
        while k <= len(nums):
            max_elements.append(max(nums[left:k]))
            left += 1
            k += 1
        return max_elements
