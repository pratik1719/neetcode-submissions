# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root and subRoot is None:
            return True
        if root is None and subRoot:
            return False
        if root is None and subRoot is None:
            return True

        def sametree(root,subRoot):
            if (root is None and subRoot) or (root and subRoot is None):
                return False
            if root is None and subRoot is None:
                return True
            if root and subRoot and root.val == subRoot.val:
                print(root.val)
                print(subRoot.val)
                if sametree(root.left,subRoot.left) and sametree(root.right,subRoot.right):
                    return True
                else:
                    return False
            

        if sametree(root, subRoot):
            return True
        if self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot):
            return True
        return False







            
        
        # start connecting the dots
        