# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        equivalent = True
        def check( p , q ):
            nonlocal equivalent
            if p is None and q is None:
                return
            if (p is not None and q is None) or (q is not None and p is None) :
                equivalent = False
                return
            if p and q and p.val != q.val:
                equivalent = False
                return   
            check(p.left,q.left)
            check(p.right,q.right)
            
        check(p,q)
        if equivalent == True:
            return True
        else:
            return False
        