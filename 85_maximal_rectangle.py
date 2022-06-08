# -*- coding: utf-8 -*-
"""
Created on Jun 08 06:12:27 2022

@author: Jerome Yutai Shen

"""
from typing import List


def leetcode84(heights):
    stack = [-1]

    maxarea = 0
    for i in range(len(heights)):

        while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
            maxarea = max(maxarea, heights[stack.pop()] * (i - stack[-1] - 1))
        stack.append(i)

    while stack[-1] != -1:
        maxarea = max(maxarea, heights[stack.pop()] * (len(heights) - stack[-1] - 1))
    return maxarea


def maximalRectangle(matrix: List[List[str]]) -> int:

    if not matrix: return 0

    maxarea = 0
    dp = [0] * len(matrix[0])
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # update the state of this row's histogram using the last row's histogram
            # by keeping track of the number of consecutive ones

            dp[j] = dp[j] + 1 if matrix[i][j] == '1' else 0

        # update maxarea with the maximum area from this row's histogram
        maxarea = max(maxarea, leetcode84(dp))
    return maxarea
