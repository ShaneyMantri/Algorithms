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

    
    ## METHOD 2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        level = 0
        if not root:
            return 
        d1 = deque([(root, 0)])
        d2 = deque([])
        
        
        d = {}
        level=1
        while d1 or d2:
            # print(d1,d2)
            print("D1",d1)
            
            if level%2==1:
                if not d1:
                    break
                while d1:
                    n,l = d1.popleft()
                    if n.left:
                        d2.append((n.left, l+1))
                    if n.right:
                        d2.append((n.right, l+1))
                    if l in d:
                        d[l].append(n.val)
                    else:
                        d[l]=[n.val]
                level+=1
            print(d2)
            if level%2==0:
                if not d2:
                    break
                while d2:
                    n,l = d2.pop()
                    if n.right:
                        d1.appendleft((n.right, l+1))
                    if n.left:
                        d1.appendleft((n.left, l+1))
                    if l in d:
                        d[l].append(n.val)
                    else:
                        d[l]=[n.val]
                level+=1
        return d.values()
                
            
        
