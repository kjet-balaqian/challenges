# -*- coding: utf-8 -*-
"""
Created on Jun 07 19:31:10 2022

@author: Jerome Yutai Shen

"""


def solveNQueens(n):
    # write your code here
    board = [['.'] * n for _ in range(n)]
    queens = [0] * n
    res = []

    def dfs(row):
        if row == n:
            res.append(generate())
            return

        for col in range(n):
            if check(row, col):
                board[row][col] = 'Q'
                queens[row] = row * 10 + col
                dfs(row + 1)
                board[row][col] = '.'

    def check(row, col):
        for i in range(row):
            q = queens[i]
            x, y = q // 10, q % 10
            if y == col or abs(row - x) == abs(col - y):
                return False
        return True

    def generate():
        return [''.join(board[i]) for i in range(n)]

    dfs(0)
    return res