/*
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.
*/
class Solution {
    int d = Integer.MAX_VALUE;
    public void dfs(TreeNode root, int p) {
        if(root.left == null && root.right ==null) {
            this.d = this.d < p? this.d : p;
            return;
        }
        if(root.left != null)
            this.dfs(root.left, p + 1);
        
        if(root.right != null)
            this.dfs(root.right, p + 1);
    }
    
    public int minDepth(TreeNode root) {
        this.d = Integer.MAX_VALUE;
        if (root == null)
            return 0;
        this.dfs(root, 1);
        return this.d;
    }
}
