'''
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
'''

class Solution:
    def inorderTraversal(self, root):
        traversal = []
        def inorderHelper(root):
            if not root:
                return
            if root.left:
                inorderHelper(root.left)
            traversal.append(root.val)
            if root.right:
                inorderHelper(root.right)

        inorderHelper(root)
        return traversal

