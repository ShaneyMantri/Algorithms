"""
 Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

    The root is the maximum number in the array.
    The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
    The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.

Construct the maximum tree by the given array and output the root node of this tree.

Example 1:

Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1


"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def construct(self, l):
        if not l:
            return
        if len(l)==1:
            return TreeNode(l[0])
            
        temp1 = l.index(max(l))
        # temp2 = nums[i+1:].index(max(nums[i+1:]))
        # print(l,temp1)
        # print(l[0:temp1], l[temp1+1:])
        l1 = self.construct(l[0:temp1])
        r = self.construct(l[temp1+1:])
        
        temp = TreeNode(l[temp1])
        temp.left = l1
        temp.right = r
        # print(temp.val)
        return temp
        
        
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if len(nums)==0:
            return []
        if len(nums)==1:
            return TreeNode(nums[0])
        i = nums.index(max(nums))
        
        root1 = self.construct(nums[0:i])
        print("Iter2")
        root2 = self.construct(nums[i+1:])
        
        root = TreeNode(nums[i])
        root.left = root1
        root.right = root2
        return root
