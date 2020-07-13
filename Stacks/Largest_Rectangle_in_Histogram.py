"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

The largest rectangle is shown in the shaded area, which has area = 10 unit.
Example:

Input: [2,1,5,6,2,3]
Output: 10
"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        if len(heights)==0:
            return 0
        
        heights = [0]+heights+[0]
        n = len(heights)
        max_area = min(heights)*n
        stack.append(0)
        
        i = 1
        while i<n:
            if stack:
                if heights[i]>=heights[stack[-1]]:
                    stack.append(i)
                else:
                    while stack and heights[i]<heights[stack[-1]]:
                        t = stack.pop()
                        if stack:
                            area = heights[t]*(i-1-stack[-1])
                            max_area= max(max_area, area)
                        else:
                            max_area = max(heights[t], max_area, )
                    stack.append(i)
            else:
                stack.append(i)
            i+=1
            
        if stack:
            while len(stack)>1:
                t = stack.pop()
                area = heights[t]*(i-1-stack[-1])
                max_area= max(max_area, area)
        return max_area




