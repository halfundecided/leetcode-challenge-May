"""
May 7, 2020
Cousins in Binary Tree
- In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
"""


def isCousins(root, x, y):
    def findDepth(parent, node, target, depth):
        if node == None:
            return -1, parent
        if node.val == target:
            return depth, parent

        right_depth, right_parent = findDepth(
            node, node.right, target, depth+1)
        left_depth, left_parent = findDepth(
            node, node.left, target, depth+1)

        if right_depth == -1:
            return left_depth, left_parent
        else:
            return right_depth, right_parent

    ###########################################################################
    if root == None:
        return False
    x_depth, x_parent = findDepth(None, root, x, 0)
    y_depth, y_parent = findDepth(None, root, y, 0)
    if (x_depth == y_depth) and (x_parent != y_parent):
        return True
    else:
        return False
