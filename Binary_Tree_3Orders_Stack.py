# -*- coding: utf-8 -*-
"""
Created on Jul 06 22:41:08 2022

@author: Jerome Yutai Shen

"""
from common_classes import BinaryTreeNode
from typing import List, Optional


RIGHT_CODE = 3
LEFT_CODE = 2
ROOT_CODE = 1
CHILD_CODE = 0


def dfs_traversal(root: Optional[BinaryTreeNode], node_print_code: int) -> List[int]:
    stack = [(root, CHILD_CODE)]
    values = []

    while stack:
        node, code = stack.pop()
        if node is None:
            continue
        print(node.val, code)

        if code == CHILD_CODE:
            stack.append((node, RIGHT_CODE))
            stack.append((node.right, CHILD_CODE))
            stack.append((node, LEFT_CODE))
            stack.append((node.left, CHILD_CODE))
            stack.append((node, ROOT_CODE))

        if code == node_print_code:
            values.append(node.val)

    return values


def dfs_traversal2(root: Optional[BinaryTreeNode], node_print_code: int) -> List[int]:
    stack = [(root, CHILD_CODE)]
    values = []

    while stack:
        node, code = stack.pop()
        if node is None:
            continue
        print(node.val, code)

        if code == CHILD_CODE:
            stack.append((node, ROOT_CODE))

            stack.append((node, LEFT_CODE))
            stack.append((node.left, CHILD_CODE))

            stack.append((node, RIGHT_CODE))
            stack.append((node.right, CHILD_CODE))

        if code == node_print_code:
            values.append(node.val)

    return values


def inorder_traversal(root: Optional[BinaryTreeNode]) -> List[int]:
    stack = [(root, 0)]
    values = []
    node_print_code = LEFT_CODE

    while stack:
        node, count = stack.pop()
        if node is None:
            continue

        if count == CHILD_CODE:
            stack.append((node, RIGHT_CODE))
            stack.append((node.right, CHILD_CODE))
            stack.append((node, LEFT_CODE))
            stack.append((node.left, CHILD_CODE))
            stack.append((node, ROOT_CODE))

        if count == node_print_code:
            values.append(node.val)

    return values


def postorder_traversal(root: Optional[BinaryTreeNode]) -> List[int]:
    stack = [(root, 0)]
    stack2 = [(root.val, 0)]
    values = []
    node_print_code = RIGHT_CODE

    while stack:
        node, count = stack.pop()
        if node is None:
            continue

        if count == CHILD_CODE:
            stack.append((node, RIGHT_CODE))
            stack.append((node.right, CHILD_CODE))
            stack.append((node, LEFT_CODE))
            stack.append((node.left, CHILD_CODE))
            stack.append((node, ROOT_CODE))

        if count == node_print_code:
            values.append(node.val)

    return values


def preorder_traversal(root: Optional[BinaryTreeNode]) -> List[int]:
    stack = [(root, 0)]
    values = []
    node_print_code = ROOT_CODE

    while stack:
        node, count = stack.pop()
        if node is None:
            continue

        if count == CHILD_CODE:
            stack.append((node, RIGHT_CODE))
            stack.append((node.right, CHILD_CODE))
            stack.append((node, LEFT_CODE))
            stack.append((node.left, CHILD_CODE))
            stack.append((node, ROOT_CODE))

        if count == node_print_code:
            values.append(node.val)

    return values


if __name__ == "__main__":
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    # root.left.left = BinaryTreeNode(4)
    # root.left.left.right = BinaryTreeNode(5)

    root.right = BinaryTreeNode(3)
    # root.right.left = BinaryTreeNode(6)
    # root.right.right = BinaryTreeNode(7)
    # root.right.right.left = BinaryTreeNode(8)

    print(dfs_traversal(root, RIGHT_CODE))
    print(dfs_traversal2(root, RIGHT_CODE))
    """
    for _ in [RIGHT_CODE, LEFT_CODE, ROOT_CODE]:
        print(dfs_traversal(root, _))

    print(inorder_traversal(root))
    print(preorder_traversal(root))
    print(postorder_traversal(root))
    """