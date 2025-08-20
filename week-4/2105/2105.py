# 2105. 디저트 카페

# import sys
# sys.stdin = open("sample_input.txt")


def cafe_tour(r, c, width, height):
    """(r, c)를 최상단으로 하는 카페 투어 경로를 탐색한다."""
    global max_desserts
    current_desserts = [cafe[r][c]]
    start = (r, c)

    # 카페 투어를 시작한다.
    for i in range(4):
        # 우하, 좌상의 경로 길이는 width
        if i % 2 == 0:
            # 직진하면서 유효한 디저트이면 탐색을 계속한다.
            for k in range(1, width+1):
                nr = r + dr[i] * k
                nc = c + dc[i] * k
                if (
                    0 <= nr < N and 0 <= nc < N 
                    and cafe[nr][nc] not in current_desserts
                ):
                    current_desserts.append(cafe[nr][nc])
                else:
                    return
        
        # 좌하, 우상의 경로 길이는 height
        else:
            for k in range(1, height+1):
                nr = r + dr[i] * k
                nc = c + dc[i] * k
                if (
                    0 <= nr < N and 0 <= nc < N 
                    and cafe[nr][nc] not in current_desserts
                ):
                    current_desserts.append(cafe[nr][nc])
                
                # 마지막에 출발지로 돌아오는 경우, 
                # 투어를 성공적으로 마쳤으므로 최대값 갱신
                elif (nr, nc) == start:
                    if len(current_desserts) > max_desserts:
                        max_desserts = len(current_desserts)
                        return
                else:
                    return

        # 방향 전환을 위해 현위치를 갱신한다.
        r, c = nr, nc



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]

    # 카페 투어를 위한 델타 (시계방향, 우하-좌하-좌상-우상 순)
    dr = [1, 1, -1, -1]
    dc = [1, -1, -1, 1]

    # 시작 위치
    r, c = 0, 0
    # 가장 많이 먹을 때의 디저트 수
    max_desserts = -1

    for r in range(N-1):
        for c in range(1, N-1):
            for width in range(1, N-1):
                for height in range(1, N-1):
                    cafe_tour(r, c, width, height)

    print(f'#{tc} {max_desserts}')
