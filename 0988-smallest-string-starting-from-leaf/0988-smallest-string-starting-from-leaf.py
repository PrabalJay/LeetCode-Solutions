# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        res=None
        path=[]
        def dfs(node):
            nonlocal res
            if not node:
                return
            path.append(chr(node.val+ord('a')))
            if not node.left and not node.right:
                s="".join(reversed(path))
                if res is None or s<res:
                    res=s
            dfs(node.left)
            dfs(node.right)
            path.pop()
        dfs(root)
        return res