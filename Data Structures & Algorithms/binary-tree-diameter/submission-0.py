# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def height(root) -> int:
            nonlocal maxi
            if root is None:
                return 0
            l = height(root.left)
            r = height(root.right)
            maxi = max(maxi,l+r)
            return 1 + max(l,r)
        maxi=0
        a = height(root)
        return maxi
        
        
        

        