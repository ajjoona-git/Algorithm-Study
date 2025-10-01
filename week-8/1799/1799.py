# 1799. 비숍

'''오답
N = int(input())
# 비숍을 놓을 수 있는 곳에는 1, 비숍을 놓을 수 없는 곳에는 0
board = [list(map(int, input().split())) for _ in range(N)]
result = 0

for r in range(N):
    for c in range(N):
        # 비숍을 놓을 수 없는 곳은 pass
        if board[r][c] == 0:
            continue

        # 1이면 비숍을 놓는다.
        result += 1
        # 현 위치와 대각선 방향은 모두 비숍을 놓을 수 없기 때문에 0으로 바꾼다.
        board[r][c] = 0
        for i in range(r + 1, N):
            for j in range(N):
                dx = r - i
                dy = c - j
                if (dx == dy) or (dx == -dy):
                    board[i][j] = 0

print(result)
'''

''' 시간초과
def dfs(board, r, c, count):
    global max_count

    # 종료 조건: 모든 좌표를 정하면 종료
    if r == N:
        max_count = max(max_count, count)
        return

    # 1. 비숍을 놓는다.
    if board[r][c] == 1:
        # 현 위치와 대각선 방향은 모두 비숍을 놓을 수 없기 때문에 0으로 바꾼다.
        new_board = [row[:] for row in board]
        new_board[r][c] = 0
        for i in range(r + 1, N):
            for j in range(N):
                dx = r - i
                dy = c - j
                if (dx == dy) or (dx == -dy):
                    new_board[i][j] = 0

        if c+1 < N:
            dfs(new_board, r, c+1, count + 1)
        else:
            dfs(new_board, r+1, 0, count + 1)

    # 2. 비숍을 놓지 않는다.
    if c+1 < N:
        dfs(board, r, c+1, count)
    else:
        dfs(board, r+1, 0, count)


N = int(input())
# 비숍을 놓을 수 있는 곳에는 1, 비숍을 놓을 수 없는 곳에는 0
board = [list(map(int, input().split())) for _ in range(N)]
max_count = 0
dfs(board, 0, 0, 0)
print(max_count)
'''


''' 시간초과
# 대각선 위치를 탐색할 델타 배열
dr = [-1, -1, 1, 1]
dc = [-1, 1, -1, 1]


def dfs(r, c, count, blocked_positions=set()):
    global max_count

    if r == N:
        max_count = max(max_count, count)
        return

    # 비숍을 놓지 않는다.
    if c+1 < N:
        dfs(r, c+1, count, blocked_positions)
    else:
        dfs(r+1, 0, count, blocked_positions)

    # 비숍을 놓는다.
    if board[r][c] == 1 and (r, c) not in blocked_positions:
        new_blocked = {(r, c)}
        for i in range(4):
            for k in range(1, N):
                nr = r + dr[i] * k
                nc = c + dc[i] * k
                if 0 <= nr < N and 0 <= nc < N:
                    new_blocked.add((nr, nc))
        if c+1 < N:
            dfs(r, c+1, count+1, blocked_positions | new_blocked)
        else:
            dfs(r+1, 0, count+1, blocked_positions | new_blocked)


N = int(input())
# 비숍을 놓을 수 있는 곳에는 1, 비숍을 놓을 수 없는 곳에는 0
board = [list(map(int, input().split())) for _ in range(N)]

# 비숍을 놓을 수 없는 위치를 저장할 set
blocked_positions = set()

max_count = 0
dfs(0, 0, 0, blocked_positions)

print(max_count)
'''

''' 시간초과
def check(r, c):
    """(r, c) 위치에 비숍을 놓을 수 있는지 확인한다."""
    # 비숍을 놓을 수 없는 곳
    if board[r][c] == 0:
        return False

    # / 대각선에 비숍이 있는지 확인
    i, j = r - 1, c + 1
    while 0 <= i and j < N:
        if visited[i][j]:
            return False
        i -= 1
        j += 1

    # \ 대각선에 비숍이 있는지 확인
    i, j = r - 1, c - 1
    while 0 <= i and 0 <= j:
        if visited[i][j]:
            return False
        i -= 1
        j -= 1

    # 양 대각선에 비숍이 없다면 True
    return True


def dfs(r, c, count):
    global max_count

    # 종료 조건: 모든 좌표를 정하면 종료
    if r == N:
        max_count = max(max_count, count)
        return

    # 행 이동
    if c+1 < N:
        # 비숍을 놓는다.
        if check(r, c):
            visited[r][c] = 1
            dfs(r, c+1, count + 1)
            visited[r][c] = 0
        # 비숍을 놓지 않는다.
        dfs(r, c+1, count)

    # 열 이동
    else:
        # 비숍을 놓는다.
        if check(r, c):
            visited[r][c] = 1
            dfs(r+1, 0, count + 1)
            visited[r][c] = 0
        # 비숍을 놓지 않는다.
        dfs(r+1, 0, count)


N = int(input())
# 비숍을 놓을 수 있는 곳에는 1, 비숍을 놓을 수 없는 곳에는 0
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

max_count = 0
dfs(0, 0, 0)
print(max_count)
'''

# board = [[1] * N for _ in range(N)]


"""
흑과 백을 나눈다..?
r + c == 짝수 or 홀수

"""
