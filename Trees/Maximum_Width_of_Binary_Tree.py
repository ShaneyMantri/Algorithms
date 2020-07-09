"""
Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

Example 1:

Input: 

           1
         /   \
        3     2
       / \     \  
      5   3     9 

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).

Example 2:

Input: 

          1
         /  
        3    
       / \       
      5   3     

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).

Example 3:

Input: 

          1
         / \
        3   2 
       /        
      5      

Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).

Example 4:

Input: 

          1
         / \
        3   2
       /     \  
      5       9 
     /         \
    6           7
Output: 8
Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).
"""
class Solution:
    d = {}
    def dfs(self, root, p, l):
        if not root:
            return
        
        self.dfs(root.left, 2*p, l+1)
        if l in self.d:
            self.d[l].append(p)
        else:
            self.d[l] = [p]
        self.dfs(root.right, 2*p +1, l+1)
            
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        self.d = {}
        if not root:
            return 0
        self.dfs(root, 1,1)
        print(self.d)
        
        m = 0
        for k,v in self.d.items():
            if m<abs(max(v)-min(v)+1):
                m = abs(max(v)-min(v)+1)
        return m
