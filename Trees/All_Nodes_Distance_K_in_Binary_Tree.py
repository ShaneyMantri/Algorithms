"""
We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.

 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation: 
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.

Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.
"""

from collections import deque
class Solution:
    def dfs(self, root, d):
        if not root:
            return
        
        if root.left:
            self.dfs(root.left, d)
            d[root] = d.setdefault(root, []) + [root.left]
            d[root.left] = d.setdefault(root.left, []) + [root]
            
        if root.right:
            self.dfs(root.right, d)
            d[root] = d.setdefault(root, []) + [root.right]
            d[root.right] = d.setdefault(root.right, []) + [root]

    def makeGraph(self, root):
        d = {}
        self.dfs(root, d)
        return d
        
    def findNodes(self, target, k, g):
        q = deque([(target, k)])
        result = []
        visited = [target]
        while q:
            n, dist = q.popleft()
            if dist == 0:
                result.append(n.val)
                continue
            else:
                if n in g:
                    for j in g[n]:
                        if j not in visited:
                            visited.append(j)
                            q.append((j, dist - 1))
        return result
        
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        if not root:
            return []
        g = self.makeGraph(root)
        return self.findNodes(target, K, g)
        
