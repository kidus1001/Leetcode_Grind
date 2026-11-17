class Solution(object):
    def hasPathSum(self, root, targetSum):
        def myFun (root, sum):
            if not root:
                return False
            sum += root.val

            if not root.left and not root.right:
                if (sum == targetSum):
                    return True
                else:
                    return False
            return myFun (root.left, sum) or myFun (root.right, sum)
        return myFun(root, 0)