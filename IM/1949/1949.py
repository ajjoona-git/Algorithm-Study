# 1949. 등산로 조성


def explore_path(r, c, current_len, is_cut_valid=True):
    """(r,c)에서 시작하는 등산로의 길이를 탐색하는 함수"""
    global longest_len

    # 최장경로 갱신
    if current_len > longest_len:
        longest_len = current_len

    # 방문한 노드 표시
    visited[r][c] = True

    # 등산로 탐색을 위한 델타 (상하좌우 순)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            # 1. 현재 위치보다 낮은 지형인 경우, keep going
            if grid[nr][nc] < grid[r][c]:
                explore_path(nr, nc, current_len + 1, is_cut_valid)

            # 2. 공사가 가능한 경우, 공사 진행 여부 확인
            # K가 (공사할 위치) - (현재 높이 - 1)보다 크거나 같다면 공사 가능.
            elif is_cut_valid and K > (grid[nr][nc] - grid[r][c]):
                # 공사하기 전 원래 높이를 저장
                original_height = grid[nr][nc]
                # 현재 높이에서 1만큼만 작게 높이를 지정한다.
                # (가장 긴 등산로를 만들기 위함)
                grid[nr][nc] = grid[r][c] - 1

                explore_path(nr, nc, current_len + 1, False)
                # 재귀를 마치고 돌아오면 다른 경로를 탐색해야 하므로 원상복구한다.
                grid[nr][nc] = original_height

    # 재귀를 마치고 돌아오면 다른 길을 탐색해야 하므로 visited를 초기화한다.
    visited[r][c] = False


T = int(input())
for tc in range(1, T+1):
    # N: 지도의 크기(NxN), K: 최대 공사 가능 깊이
    N, K = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]

    # 가장 높은 봉우리의 높이 찾기
    max_height = 0
    for r in range(N):
        for c in range(N):
            if grid[r][c] > max_height:
                max_height = grid[r][c]
    
    # 가장 긴 경로의 길이 찾기
    longest_len = 0
    # 가장 높은 봉우리를 출발지로 한다.
    for r in range(N):
        for c in range(N):
            if grid[r][c] == max_height:
                explore_path(r, c, 1, True)
    
    print(f'#{tc} {longest_len}')