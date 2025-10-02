import sys
input = sys.stdin.readline
import math as Math


n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
line1 = ['W','B'] * 4
line2 = ['B','W'] * 4
chess1 = [line1, line2] * 4
chess2 = [line2, line1] * 4
minnum = 64

for i in range(n - 7):
    for j in range(m - 7):
        sub_board = [row[j:j+8] for row in board[i:i+8]]
        count1 = sum(sub_board[x][y] != chess1[x][y] for x in range(8) for y in range(8))
        count2 = sum(sub_board[x][y] != chess2[x][y] for x in range(8) for y in range(8))
        repaint = min(count1, count2)
        if repaint < minnum:
            minnum = repaint

print(minnum)