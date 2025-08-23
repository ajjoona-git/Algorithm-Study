# 1868. 파핑파핑 지뢰 찾기

# 인접한 8방향 탐색을 위한 델타 (12시부터 시계방향으로)
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]


def find_mines(r, c):
    # 주변에 지뢰가 있는지 확인한다.
    # visited[r][c] = 1
    for i in range(8):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] == '*':
            return 1  # 지뢰가 있다면 1 반환
    return 0  # 지뢰가 없으면 0 반환
    
def visit_zero(r, c):
    # 0인 칸(주변에 지뢰가 없음)에 방문했다면 인접한 8방향을 탐색한다.
    visited[r][c] = 1
    for i in range(8):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
            visited[nr][nc] = 1
            grid[nr][nc] = find_mines(r + dr[i], c + dc[i])
            # 탐색 중 0인 칸이 있다면 해당 칸의 인접 칸을 다시 탐색한다.
            if grid[nr][nc] == 0:
                visit_zero(nr, nc)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    grid = [list(input().strip()) for _ in range(N)]
    # visit_zero를 통해 탐색한 칸은 '1'로 표시
    visited = [[0] * N for _ in range(N)]
    result = 0

    # 현 위치 (r, c)를 순회하면서 숫자 정보를 저장한다.
    for r in range(N):
        for c in range(N):
            # 1. 지뢰가 아니고 아직 탐색하지 않았다면 숫자를 표시한다.
            if grid[r][c] == '.' and visited[r][c] == 0:
                grid[r][c] = find_mines(r, c)
                # 주변에 지뢰가 없으면(0), 인접 그리드에 대해서 지뢰 찾기
                if grid[r][c] == 0:
                    result += 1
                    visit_zero(r, c)
            
            # 2. 이미 탐색한 곳이거나, 지뢰일 때는 그냥 지나간다.
            else:
                continue


    # 지금까지 계산된 result값은 0으로 이루어진 덩어리의 수
    for r in range(N):
        for c in range(N):
            # 개별 숫자 칸을 더해준다.
            if visited[r][c] == 0 and grid[r][c] == 1:
                result += 1
    
    
    print(f'#{tc} {result}')