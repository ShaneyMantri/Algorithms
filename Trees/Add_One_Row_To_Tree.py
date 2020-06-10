"""
Given the root of a binary tree, then value v and depth d, you need to add a row of nodes with value v at the given depth d. The root node is at depth 1.

The adding rule is: given a positive integer depth d, for each NOT null tree nodes N in depth d-1, create two tree nodes with value v as N's left subtree root and right subtree root. And N's original left subtree should be the left subtree of the new left subtree root, its original right subtree should be the right subtree of the new right subtree root. If depth d is 1 that means there is no depth d-1 at all, then create a tree node with value v as the new root of the whole original tree, and the original tree is the new root's left subtree.

Example 1:

Input: 
A binary tree as following:
       4
     /   \
    2     6
   / \   / 
  3   1 5   

v = 1

d = 2

Output: 
       4
      / \
     1   1
    /     \
   2       6
  / \     / 
 3   1   5   

Example 2:

Input: 
A binary tree as following:
      4
     /   
    2    
   / \   
  3   1    

v = 1

d = 3

Output: 
      4
     /   
    2
   / \    
  1   1
 /     \  
3       1

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def addOneRow(self, root: TreeNode, v: int, m: int) -> TreeNode:
        if m==1:
            t1 = TreeNode(v)
            t1.left=root
            t1.right=None
            return t1
        d = deque()
        d.append([root, 1])
        
        while d:
            temp = d.popleft()
            if temp[1]>(m-1):
                break
            if temp[1]==m-1:
                t1 = TreeNode(v)
                t1.left = temp[0].left
                temp[0].left = t1
                t2 = TreeNode(v)
                t2.right = temp[0].right
                temp[0].right = t2
                d.append([t1,temp[1]+1])
                d.append([t2, temp[1]+1])
            else:
                if temp[0].left:
                    d.append([temp[0].left, temp[1]+1])
                if temp[0].right:
                    d.append([temp[0].right, temp[1]+1])
        return root
