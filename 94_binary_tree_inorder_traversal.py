# -*- coding: utf-8 -*-
"""
Created on Jun 08 11:41:02 2022

@author: Jerome Yutai Shen

"""
from common_classes import BinaryTreeNode
from typing import List, Optional


class Solution:
    def inorderTraversal(self, root: Optional[BinaryTreeNode]) -> List[int]:
        if not root:
            return []

        stack = []
        curr_node = root
        nodes_values_list = []
        while stack or curr_node:
            print(f"stack: {stack}, curr_node: {curr_node}\n")
            if curr_node:
                stack.append(curr_node)
                curr_node = curr_node.left
            else:
                node = stack.pop()
                nodes_values_list.append(node.val)
                curr_node = node.right
        return nodes_values_list