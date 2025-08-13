# 20739: 고대 유적 2


T = int(input())
for tc in range(1, T+1):
    # NxM 배열
    N, M = map(int, input().split())
    grid = [input().split() for _ in range(N)]
    
    # 가로 방향
    max_len_h = 0
    for row in grid:
        current_len = 0
        for char in row:
            if char == '1':
                current_len += 1
            else:
                max_len_h = max(current_len, max_len_h)
                current_len = 0
        max_len_h = max(current_len, max_len_h)

    # 세로 방향
    max_len_v = 0
    for c in range(M):
        current_len = 0
        for r in range(N):
            if grid[r][c] == '1':
                current_len += 1
            else:
                max_len_v = max(current_len, max_len_v)
                current_len = 0
        max_len_v = max(current_len, max_len_v)

    # 최대 길이 계산
    max_len = max(max_len_h, max_len_v)
    if max_len <= 1:
        max_len = 0

    print(f'#{tc} {max_len}')