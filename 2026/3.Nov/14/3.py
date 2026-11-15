class Solution(object):
    def inorderTraversal(self, root):
        res = []
        def inorderTraversall (root):
            if root is None:
                return
            inorderTraversall (root.left)
            res.append(root.val)
            inorderTraversall (root.right)
        
        inorderTraversall (root)
        return res