class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        maxA = 0
        while l < r:
            tmp = min(heights[l], heights[r]) * (r - l)
            maxA = max(maxA, tmp)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxA