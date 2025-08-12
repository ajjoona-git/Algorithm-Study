# 23795: 우주 괴물

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # grid: 구역 정보
    # 0 (빈칸), 1 (벽), 2 (괴물)
    grid = [input().split() for _ in range(N)]

    # 광선 발사 방향 (상하좌우 순)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 괴물의 위치
    for r in range(N):
        for c in range(N):
            if grid[r][c] == '2':
                monster = (r, c)

    # 광선 발사
    for i in range(4):
        for k in range(1, N):
            nr = monster[0] + dr[i] * k
            nc = monster[1] + dc[i] * k

            # 현위치가 벽에 막히지 않고 빈칸(0)이라면 '2'로 바꿔서 안전하지 않음을 표시한다.
            if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] == '0':
                grid[nr][nc] = '2'
            else:
                break
    
    # 안전한 구역
    safety_zone = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] == '0':
                safety_zone += 1

    print(f'#{tc} {safety_zone}')