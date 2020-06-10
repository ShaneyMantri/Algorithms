"""
Given a binary tree, return the sum of values of its deepest leaves.

Example 1:

Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15


"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        res = []
        d = {}
        if not root:
            return 0
        queue = deque()
        queue.append((root, 0))
        d[0]=[root.val]
        while queue:
            temp = queue.popleft()
            # print(temp[0].val)
            if temp[0].left:
                if (temp[1]+1) not in d:
                    d[temp[1]+1] = temp[0].left.val
                else:
                    d[temp[1]+1]+=temp[0].left.val
                queue.append((temp[0].left, temp[1]+1))
            if temp[0].right:
                if (temp[1]+1) not in d:
                    d[temp[1]+1] = temp[0].right.val
                else:
                    d[temp[1]+1]+=temp[0].right.val
                queue.append((temp[0].right, temp[1]+1))
                
        return d[max(d.keys())]
        
        
        
        
        
        
