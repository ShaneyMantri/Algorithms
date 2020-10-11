"""
You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. 
It is guaranteed that the new value does not exist in the original BST.
Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.
"""
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        t = root
        if root is None:
            return TreeNode(val)
        
        while t is not None:
            if t.val < val:
                if t.right:
                    t = t.right
                else:
                    t.right = TreeNode(val)
                    return root
            else:
                if t.left:
                    t = t.left
                else:
                    t.left = TreeNode(val)
                    return root
                
            
        
