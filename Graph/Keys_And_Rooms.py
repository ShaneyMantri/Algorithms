"""
There are N rooms and you start in room 0.  Each room has a distinct number in 0, 1, 2, ..., N-1, and each room may have some keys to access the next room. 

Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is an integer in [0, 1, ..., N-1] where N = rooms.length.  A key rooms[i][j] = v opens the room with number v.

Initially, all the rooms start locked (except for room 0). 

You can walk back and forth between rooms freely.

Return true if and only if you can enter every room.

Example 1:

Input: [[1],[2],[3],[]]
Output: true
Explanation:  
We start in room 0, and pick up key 1.
We then go to room 1, and pick up key 2.
We then go to room 2, and pick up key 3.
We then go to room 3.  Since we were able to go to every room, we return true.
Example 2:

Input: [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can't enter the room with number 2.
"""

class Solution:
    def makeGraph(self, rooms):
        d = {}
        for i in range(len(rooms)):
            d[i] = rooms[i].copy()
        return d
    
    def dfs(self, g, v, i):
        if i in g:
            for j in g[i]:
                if v[j] == 0:
                    v[j] = 1
                    self.dfs(g, v, j)
        
            
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        g = self.makeGraph(rooms)
        v = [0]*len(rooms)
        v[0] = 1
        self.dfs(g, v, 0)
        return True if min(v) == 1 else False
        
