"""
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level X such that the sum of all the values of nodes at level X is maximal.

Input: [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
"""

from collections import deque
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        level = {}
        if not root:
            return 0
        d = deque([(root, 1)])
        while d:
            n, l = d.popleft()
            level[l] = level.setdefault(l, 0)+n.val
            if n.left:
                d.append((n.left, l+1))
            if n.right:
                d.append((n.right, l+1))
        s = -1*(10**13)
        res = 0
        for k,v in level.items():
            if v>s:
                s = v
                res=k
        return res
                
