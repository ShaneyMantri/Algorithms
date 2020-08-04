"""
Given a binary tree root, a ZigZag path for a binary tree is defined as follow:

    Choose any node in the binary tree and a direction (right or left).
    If the current direction is right then move to the right child of the current node otherwise move to the left child.
    Change the direction from right to left or right to left.
    Repeat the second and third step until you can't move in the tree.

Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.

 

Example 1:

Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1,null,1]
Output: 3
Explanation: Longest ZigZag path in blue nodes (right -> left -> right).

Example 2:

Input: root = [1,1,1,null,1,null,null,1,1,null,1]
Output: 4
Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).

Example 3:

Input: root = [1]
Output: 0
"""
class Solution:
    def dfs(self, root, path, prev):
        if not root:
            return path
        ans = -1
        if prev=="left":
            ans = self.dfs(root.right, path+1, "right")
            ans = max(ans, self.dfs(root.left, 0, "left"))
            
        if prev=="right":
            ans = self.dfs(root.left, path+1, "left")
            ans = max(ans, self.dfs(root.right, 0, "right"))
        
        return ans


    def longestZigZag(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.dfs(root, -1, "left"), self.dfs(root, -1, "right"))
