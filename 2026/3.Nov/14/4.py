class Solution(object):
    def hasPathSum(self, root, targetSum):
        def helperFunction (root, sum):
            if root is None:
                return False
            sum += root.val

            if root.left is None and root.right is None:
                if sum == targetSum:
                    return True
                else:
                    return False
            return helperFunction (root.left,sum) or helperFunction (root.right, sum)

        return helperFunction (root, 0)