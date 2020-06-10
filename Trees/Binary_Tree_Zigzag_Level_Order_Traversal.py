"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
]

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        d1 = deque()
        d2 = deque()
        if not root:
            return []
        d1.appendleft((root,0))
        res = {}
        while d1:
            # print(d1)
            # print(d2)
            # print(res)
            # print("\n")
            temp = d1.popleft()
            if temp[1]%2==0:
                if temp[0].left:
                    d2.appendleft((temp[0].left, temp[1]+1))
                if temp[0].right:
                    d2.appendleft((temp[0].right, temp[1]+1))
            else:
                if temp[0].right:
                    d2.appendleft((temp[0].right, temp[1]+1))
                if temp[0].left:
                    d2.appendleft((temp[0].left, temp[1]+1))
            
            
            if temp[1] in res:
                res[temp[1]].append(temp[0].val)
            else:
                res[temp[1]] = [temp[0].val]
            if not d1:
                t1 = d1.copy()
                d1 = d2.copy()
                d2 = t1.copy()
            
        # print(res)
        ret = []
        for k,v in res.items():
            ret.append(v)
        print(ret)
        return ret
