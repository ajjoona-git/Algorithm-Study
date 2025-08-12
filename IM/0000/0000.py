# 기출. 경비병

import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    # N: 공간의 넓이
    N = int(input())
    # gird: 공간 데이터 (NxN)
    # 0: 빈 공간, 1: 기둥, 2: 경비병
    grid = [input().split() for _ in range(N)]

    # guard: 경비병의 위치
    for r in range(N):
        for c in range(N):
            if grid[r][c] == '2':
                guard = (r, c)
    
    # 경비병이 관찰할 방향 벡터 (상하좌우 순)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 경비병의 현 위치(guard)에서 4방향 관찰
    # 경비병은 본인위치에서 상하좌우 N만큼 관찰 가능
    # 단, 기둥 뒤는 인식하지 못함
    for i in range(4):
        for step in range(1, N):
            nr = guard[0] + dr[i] * step
            nc = guard[1] + dc[i] * step
            # 벽과 기둥 체크
            if not (0 <= nr < N and 0 <= nc < N) or grid[nr][nc] == '1':
                break
            # 관찰한 공간이 '0'(빈 공간)이면 '1'로 바꾸어 더 이상 탐색하지 못하도록 바꾼다.
            else:
                grid[nr][nc] = '1'

    # 이제 경비병이 관찰 가능한 공간은 '1'로 바뀌었기 때문에
    # grid에서 '0'인 공간은 경비병의 눈을 피할 수 있는 공간이다.
    safe_zone = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] == '0':
                safe_zone += 1

    print(f'#{tc} {safe_zone}')