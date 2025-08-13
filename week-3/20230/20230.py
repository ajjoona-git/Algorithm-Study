# 20230: 풍선팡 보너스 게임 2 

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    # 4방향 탐색을 위한 델타 (상하좌우 순)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    max_score = 0

    for r in range(N):
        for c in range(N):
            current_score = grid[r][c]
            # 4방향 탐색
            for i in range(4):
                for k in range(1, N):
                    nr = r + dr[i] * k
                    nc = c + dc[i] * k

                    # 벽 체크
                    if 0 <= nr < N and 0 <= nc < N:
                        current_score += grid[nr][nc]
                    else:
                        break
            
            max_score = max(max_score, current_score)

    print(f'#{tc} {max_score}')