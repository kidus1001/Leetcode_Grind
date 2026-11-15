class Solution(object):
    def preorderTraversal(self, root):
        res = []
        def preorderTraversall (root):
            if root is None:
                return
            res.append(root.val)
            preorderTraversall (root.left)
            preorderTraversall (root.right)
        preorderTraversall (root)
        return res