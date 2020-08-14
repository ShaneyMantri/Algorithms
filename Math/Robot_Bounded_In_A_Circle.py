"""
On an infinite plane, a robot initially stands at (0, 0) and faces north.  The robot can receive one of three instructions:

"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degress to the right.
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

 

Example 1:

Input: "GGLLGG"
Output: true
Explanation: 
The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
Example 2:

Input: "GG"
Output: false
Explanation: 
The robot moves north indefinitely.
Example 3:

Input: "GL"
Output: true
Explanation: 
The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...
"""

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        init = [0,0]
        dirs = ["N","E","S","W"]
        d = dirs[0]
        s = instructions
        v = 0
        h = 0
        for i in s:
            if i=="G":
                if d=="N":
                    v+=1
                elif d=="S":
                    v-=1
                elif d=="W":
                    h-=1
                else:
                    h+=1
            else:
                if i=="R":
                    d = dirs[(dirs.index(d)+1)%4]
                else:
                    d = dirs[(dirs.index(d)-1)%4]
        if d==dirs[0] and (h!=0 or v!=0):
            return False
        else:
            return True
