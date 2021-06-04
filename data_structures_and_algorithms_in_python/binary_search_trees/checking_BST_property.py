def is_bst_satisfied(self):
    def helper(node, lower=float('-inf'), upper=float('inf')):
        if not node:
            return True
        
        val = node.data
        if val <= lower or val >= upper:
            return False

        if not helper(node.right, val, upper):
            return False
        if not helper(node.left, lower, val):
            return False
        return True

    return helper(self.root)