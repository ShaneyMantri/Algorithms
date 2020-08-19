"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped.
Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""

class Solution:
    def trap(self, heights: List[int]) -> int:
        if len(heights)<=2:
            return 0
        left = [0]*len(heights)
        right = [0]*len(heights)
        lmax = 0
        for i in range(len(heights)):
            if lmax<heights[i]:
                left[i] = lmax
                lmax = heights[i]
            else:
                left[i] = lmax
        rmax = 0     
        for i in range(len(heights)-1, -1, -1):
            if heights[i]>rmax:
                right[i] = rmax
                rmax = heights[i]
            else:
                right[i] = rmax
                
        fin = 0
        for i in range(len(heights)):
            fin+=max(min(left[i], right[i])-heights[i], 0)
        return fin
        
