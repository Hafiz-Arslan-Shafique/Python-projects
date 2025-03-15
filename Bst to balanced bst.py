## Now, take the sorted list and recursively build a balanced BST:
## The middle element is 10, so 10 becomes the root.
## The left half of the list [3, 5, 7] becomes the left subtree, with the middle element 5 as the root.
## The right half of the list [15, 18] becomes the right subtree, with the middle element 15 as the root.




# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def bst_to_balanced_bst(root):
#     sorted_elements = inorder_traversal(root)     # Step 1: Get the elements of the BST in sorted order
#     return sorted_array_to_bst(sorted_elements)    # Step 2: Convert the sorted list to a balanced BST
    
# def inorder_traversal(root):   ## to sort element 
#     if not root:
#         return []
#     return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

# def sorted_array_to_bst(nums):
#     if not nums:
#         return None
#     mid = len(nums) // 2       
#     root = TreeNode(nums[mid])  ## to find middle element as root
#     root.left = sorted_array_to_bst(nums[:mid])   ## The left subtree is created by recursively calling sorted_array_to_bst on the left half of the array
#     root.right = sorted_array_to_bst(nums[mid+1:])  ##the right subtree is created by calling sorted_array_to_bst(nums[mid+1:]).
#     return root



# def print_inorder(root):
#     if root:
#         print_inorder(root.left)
#         print(root.val, end=" ")
#         print_inorder(root.right)

# ##Example usage:
# root = TreeNode(10)
# root.left = TreeNode(5)
# root.right = TreeNode(15)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(7)
# root.right.right = TreeNode(18)
# balanced_bst = bst_to_balanced_bst(root)

# print_inorder(balanced_bst)










##-------- when we give list
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def inorder_traversal(root):
#     if not root:
#         return []
#     return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

# def sorted_array_to_bst(nums):
#     if not nums:
#         return None
#     mid = len(nums) // 2
#     root = TreeNode(nums[mid])
#     root.left = sorted_array_to_bst(nums[:mid])
#     root.right = sorted_array_to_bst(nums[mid+1:])
#     return root

# # Example to convert the BST [4, 7, 9, 6, 3, 8] into a balanced BST:
# elements = [3, 4, 6, 7, 8, 9]  # Sorted elements from the original BST
# balanced_bst = sorted_array_to_bst(elements)

# # Inorder traversal to print the balanced BST
# def print_inorder(root):
#     if root:
#         print_inorder(root.left)
#         print(root.val, end=" ")
#         print_inorder(root.right)

# print_inorder(balanced_bst)




