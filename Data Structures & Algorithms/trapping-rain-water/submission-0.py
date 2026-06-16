class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        LMax = height[left]
        RMax = height[right]
        water = 0
        while left < right :
            if LMax < RMax :
                left += 1
                LMax = max(LMax,height[left])
                water += LMax - height[left]
            else:
                right -= 1
                RMax = max(RMax,height[right])
                water += RMax - height[right]

        return water
