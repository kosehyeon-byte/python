col, row = map(int, input().split())
matrix = [list(input().strip()) for _ in range(row)]

for r in range(row):
    for c in range(col):
        if matrix[r][c] == '*':
            continue
        count = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and matrix[nr][nc] == '*':
                    count += 1
        matrix[r][c] = str(count)

for line in matrix:
    print(''.join(line))