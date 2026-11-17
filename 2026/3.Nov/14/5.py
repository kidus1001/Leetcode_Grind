# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        def equalCheck (root, root1):
            if not root:
                return True
            if not root.left and not root.right and not root1.left and not root1.right:
                return True

            if root.right and not root1.left:
                return False
            
            if root.left and not root1.right:
                return False

            
            if root.left:
                if root.left.val != root1.right.val:
                    return False
            elif root.right:
                if root.right.val != root1.left.val:
                    return False

            return equalCheck (root.left, root1.right) and equalCheck (root.right, root1.left)

        return equalCheck (root, root)

        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        