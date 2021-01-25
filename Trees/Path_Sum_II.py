""""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1


Return:

[
   [5,4,11,2],
   [5,8,4,5]
]



"""
class Solution:
    ans = []
    def dfs(self, root, l, s):
        if s == 0 and root.left == None and root.right == None:
            self.ans.append(l)
            
        if root.left:
            self.dfs(root.left, l+[root.left.val], s-root.left.val)
        if root.right:
            self.dfs(root.right, l+[root.right.val], s-root.right.val)
                
    def pathSum(self, root: TreeNode, s: int) -> List[List[int]]:
        self.ans = []
        if not root:
            return []
        self.dfs(root, [root.val], s-root.val)
        return self.ans
