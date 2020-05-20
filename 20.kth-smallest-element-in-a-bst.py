"""
May 20, 2020
Kth Smallest Element in a BST
"""


def kthSmallest(root, k):
    if root == None:
        return None

        arr = []

        def inOrder(root, arr):
            if root:
                inOrder(root.left, arr)
                arr.append(root.val)
                inOrder(root.right, arr)
            return arr

        arr = inOrder(root, arr)

        return arr[k-1]
