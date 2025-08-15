# 4613. 러시아 국기 같은 깃발 


def coloring(white, blue, N):
    """
    흰색, 파란색, 빨간색 범위가 주어질 때, 칠해야 하는 칸의 수를 반환하는 함수
    white: 흰색으로 칠해진 마지막 행
    blue: 파란색으로 칠해진 마지막 행
    N: 행의 수
    """
    # 칠해야 하는 칸의 개수
    color = 0

    # 흰색 (0 ~ white)
    for r in range(white+1):
        for c in range(M):
            if flag[r][c] != 'W':
                color += 1

    # 파란색 (white+1 ~ blue)
    for r in range(white+1, blue+1):
        for c in range(M):
            if flag[r][c] != "B":
                color += 1

    # 빨간색 (blue+1 ~ N-1)
    for r in range(blue+1, N):
        for c in range(M):
            if flag[r][c] != "R":
                color += 1    

    return color


T = int(input())
for tc in range(1, T+1):
    N ,M = map(int, input().split())
    # flag: 초기 깃발의 색깔 정보 (NxM)
    flag = [input() for _ in range(N)]

    # 최소값
    min_color = N * M

    # 색깔 범위 정하기
    # w: 흰색(W)으로 칠해질 수 있는 행의 범위 (0 ~ N-3)
    # b: 파란색(B)으로 칠해잴 수 있는 행의 범위 (w+1 ~ N-2)
    # 빨간색(R)으로 칠해질 수 있는 행의 범위 (b+1 ~ N-1)
    for w in range(N-2):
        for b in range(w+1, N-1):
            # 색칠하기
            color = coloring(w, b, N)
            # 최소값 갱신
            if color < min_color:
                min_color = color
    
    print(f'#{tc} {min_color}')