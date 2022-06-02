# -*- coding: utf-8 -*-
"""
Created on May 29 21:48:13 2022

@author: Jerome Yutai Shen

"""
from typing import Optional


class ListNode:

    def __init__(self, val: int, next: Optional[None] = None):
        self.val = val
        self.next = next


class BinaryTreeNode:
    def __init__(self, val: int = 0, left: Optional[None] = None, right: Optional[None] = None, next: Optional[None] = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next