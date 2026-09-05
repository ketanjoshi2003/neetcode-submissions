class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_w = 0

        while left < right:
            water = (right - left) * min(heights[right], heights[left])
            max_w = max(max_w, water)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return max_w



        