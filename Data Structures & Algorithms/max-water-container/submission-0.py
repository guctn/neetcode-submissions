class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_amount = 0

        while left < right:
            min_height = min(heights[left], heights[right])
            width = right - left
            max_amount = max(max_amount, min_height * width)

            if heights[right] > heights[left]:
                left += 1
            else:
                right -= 1
        
        return max_amount

