class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def addNode(root, x):
    if x == root.val:
        return
    if x > root.val:
        if not root.right:
            root.right = TreeNode(x)
        else:
            addNode(root.right, x)
    if x < root.val:
        if not root.left:
            root.left = TreeNode(x)
        else:
            addNode(root.left, x)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)

def height(root):
    if not root:
        return 0
    lheight = height(root.left)
    rheight = height(root.right)
    max_height = max(lheight, rheight)
    return max_height + 1

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(2)
root.left.right = TreeNode(6)
root.right.left = TreeNode(13)
root.right.right = TreeNode(20)

postorder(root)
