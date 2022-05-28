# -*- coding: utf-8 -*-
"""
Created on May 22 15:19:28 2022

@author: Jerome Yutai Shen

"""


def longestPalindrome( src_str: str) -> str:
    if not src_str:
        return src_str

    end_start = (0, 0) # 终止idx在前，起始idx在后，因为下面for循环里用max比较tuple/list，比较逻辑是按照元素顺序依次比较。
    for center_idx in range(len(src_str)):
        end_start = max(end_start, get_index_range(src_str, center_idx, center_idx))
        end_start = max(end_start, get_index_range(src_str, center_idx, center_idx + 1))

    return src_str[end_start[1]: end_start[0] + end_start[1]]


def get_index_range(src_str: str, idx_left: int, idx_right: int) -> tuple:
    while idx_left >= 0 and idx_right < len(src_str) and src_str[idx_left] == src_str[idx_right]:
        idx_left -= 1
        idx_right += 1
    return idx_right - idx_left - 1, idx_left + 1