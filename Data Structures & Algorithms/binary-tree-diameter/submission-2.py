# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        map = {None: (0, 0)}
        
        while stack:
            node = stack[-1]
            
            if node.left and node.left not in map:
                stack.append(node.left)
            elif node.right and node.right not in map:
                stack.append(node.right)
            else:
                stack.pop()

                lHeight, lDiameter = map[node.left]
                rHeight, rDiameter = map[node.right]
                
                height = 1 + max(lHeight, rHeight)
                diameter = max(lHeight + rHeight, lDiameter, rDiameter)
                map[node] = (height, diameter)
        return map[root][1]

    
    
        
        
