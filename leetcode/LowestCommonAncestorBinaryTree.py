'''

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary search tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself
             according to the LCA definition.
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root in (None, p, q):
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        else:
            return left or right

        '''
        def search(root, path):
            if root.val == node.val:
                return path
            if not root.left and not root.right:
                return []
            if root.left:
                path_l = search(root.left, node, path + [(root.val,'l')])
            if root.right:
                path_r = search(root.right, node, path + [(root.val, 'r')])

            if path_l:
                return path_l
            if path_r:
                return path_r
            else:
                return []

        path_p = search(root, p, [])
        path_q = search(root, q, [])
        print(path_p)
        print(path_q)
        for i in range(min(len(path_p), len(path_q))):
            if path_p[i][0] == q.val:
                return q.val
            if path_q[i][0] == p.val:
                return p.val
            if path_p[i][1] != path_q[i][1]:
                return path_p[i][0]
        if len(path_p) < len(path_q):
            return p.val
        else:
            return q.val
        '''

sol = Solution()
root = TreeNode(3)
root.left = TreeNode(5)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right = TreeNode(1)
root.right.right = TreeNode(8)
root.right.left = TreeNode(0)
print(sol.lowestCommonAncestor(root, root.left, root.left.right.right).val)


