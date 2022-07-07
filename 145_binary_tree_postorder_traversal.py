# -*- coding: utf-8 -*-
"""
Created on Jul 06 16:47:46 2022

@author: Jerome Yutai Shen

"""
from common_classes import BinaryTreeNode
from typing import List, Optional


def postorder_traversal(root: Optional[BinaryTreeNode]) -> List[int]:
    if root is None:
        return []
    stack = [root]
    result = []
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.left is not None:
            stack.append(node.left)
        if node.right is not None:
            stack.append(node.right)
    print(result)
    return result[::-1]


if __name__ == "__main__":
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.left.left = BinaryTreeNode(4)
    root.left.left.right = BinaryTreeNode(5)

    root.right = BinaryTreeNode(3)
    root.right.left = BinaryTreeNode(6)
    root.right.right = BinaryTreeNode(7)
    root.right.right.left = BinaryTreeNode(8)

    nodes_values_list = postorder_traversal(root)
    print(nodes_values_list)