# 기출 복원. 차르 봄바

import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    # grid: 각 지역의 위력이 저장된 NxM 크기의 배열. 
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    # 폭탄의 영향권 4방향 (상하좌우 순)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    max_power = 0  # 위력의 최대값

    # 현재 위치를 이동하면서 폭탄의 위력을 계산한다.
    for r in range(N):
        for c in range(M):
            # 현재 위치의 위력이 곧 폭탄의 영향 범위
            P = grid[r][c]
            current_power = P

            # i: 탐색할 방향
            for i in range(4):
                # k: 현재 위치와 탐색 위치의 거리
                for k in range(1, P+1):
                    nr = r + dr[i] * k
                    nc = c + dc[i] * k
                    if 0 <= nr < N and 0 <= nc < M:
                        current_power += grid[nr][nc]

            max_power = max(current_power, max_power)

    print(f"#{tc} {max_power}")