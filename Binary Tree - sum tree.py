class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def convert_to_sum_tree(root):
    if not root:
        return 0
    
    # Recursively convert left and right subtrees
    left_sum = convert_to_sum_tree(root.left)
    right_sum = convert_to_sum_tree(root.right)
    
    sum_off_all_val = left_sum + right_sum
    return sum_off_all_val + root.val

# Example usage:
root = TreeNode(10)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

print(convert_to_sum_tree(root))

# After conversion, root will have updated values based on sum tree rules.
