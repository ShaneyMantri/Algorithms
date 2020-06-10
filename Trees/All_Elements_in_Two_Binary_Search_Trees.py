"""
Given two binary search trees root1 and root2.

Return a list containing all the integers from both trees sorted in ascending order.

 

Example 1:

Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]

Example 2:

Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
Output: [-10,0,0,1,2,5,7,10]

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        d = {}
        
        def inorder(root):
            if not root:
                return
            if root.val not in d:
                d[root.val]=1
            else:
                d[root.val]+=1
            inorder(root.left)
            inorder(root.right)
                  
        inorder(root1)
        inorder(root2)
        res = []
        ds = sorted(d.items(), key=lambda kv:kv[0])
        for i in ds:
            res+=[i[0]]*i[1]
            
        return res
