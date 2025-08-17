# 1258. 행렬찾기

import sys
sys.stdin = open("input.txt")


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    # 방문 여부
    visited = [[False] * N for _ in range(N)]
    # 찾아낸 행렬들의 정보
    chemicals = []

    for r in range(N):
        for c in range(N):
            # 화학물질을 발견하면 용기의 크기 탐색 시작
            if grid[r][c] > 0 and not visited[r][c]:
                r_len = 0
                c_len = 0

                # 높이 계산
                nr = r
                while 0 <= nr < N and grid[nr][c] > 0:
                    r_len += 1
                    nr += 1

                # 너비 계산
                nc = c
                while 0 <= nc < N and grid[r][nc] > 0:
                    c_len += 1
                    nc += 1
            
                # 방문 처리
                for x in range(r, nr):
                    for y in range(c, nc):
                        visited[x][y] = True

                # 찾아낸 행렬 정보에 추가
                chemicals.append((r_len, c_len))

    # 행렬의 크기를 기준으로 오름차순으로 정렬
    chemicals.sort(key=lambda x: (x[0] * x[1], x[0]))

    print(f'#{tc} {len(chemicals)}', end=' ')
    for height, width in chemicals:
        print(height, width, end=' ')
    print()