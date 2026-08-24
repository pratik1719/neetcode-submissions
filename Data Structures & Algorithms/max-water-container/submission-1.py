class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area = small height(height[i]) * width (index diff)

        max_area =0
        i=0
        j= len(heights)-1

        while(i<j):
            area = (min(heights[i], heights[j])) * (j-i)
            if area > max_area:
                max_area = area
            if heights[i] <= heights[j]:
                i+=1
            elif heights[i] > heights[j]:
                j-=1
        return max_area







        
        