class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxWater = 0
        a = 0
        b = len(heights) - 1

        while a < b:


            currentWater = ((b-a)) * min(heights[a], heights[b])


            if currentWater > maxWater:
                maxWater = currentWater

            if heights[a] < heights[b]:
                a += 1

            elif heights[b] < heights[a]:
                b -= 1

            elif heights[a] == heights[b]:
                a += 1
                b -= 1

        
        return maxWater
         