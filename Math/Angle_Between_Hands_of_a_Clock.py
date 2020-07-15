"""Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand.

 

Example 1:

Input: hour = 12, minutes = 30
Output: 165

Example 2:

Input: hour = 3, minutes = 30
Output: 75

Example 3:

Input: hour = 3, minutes = 15
Output: 7.5

Example 4:

Input: hour = 4, minutes = 50
Output: 155

Example 5:

Input: hour = 12, minutes = 0
Output: 0
"""
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angle = hour*30-(5.5)*minutes
        if angle<0:
            return min(((-1)*angle)%360, angle+360)
        else:
            return min(angle%360, 360-angle)
        
