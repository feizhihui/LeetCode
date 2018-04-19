# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        ix = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:1 + ix], inorder[:ix])
        root.right = self.buildTree(preorder[1 + ix:], inorder[ix + 1:])

        return root