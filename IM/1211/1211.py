# 1211. Ladder2

# import sys
# sys.stdin = open("input.txt")

def calculate_length(ladder, x):
    """(0, x)에서 시작하는 경로의 길이를 반환하는 함수"""
    length = 1
    r, c = 0, x
    
    # 방문 체크
    visited = [[False] * N for _ in range(N)]

    # 사다리타기 위한 델타 (좌우하 순)
    dr = [0, 0, 1]
    dc = [-1, 1, 0]

    # 사다리 바닥에 도착할 때까지 델타 탐색
    while r < N - 1:
        for i in range(3):
            nr = r + dr[i]
            nc = c + dc[i]
            if (
                0 <= nr < N and 0 <= nc < N 
                and ladder[nr][nc] == '1' 
                and not visited[nr][nc]
            ):
                visited[nr][nc] = True
                length += 1
                r, c = nr, nc
                break
        
    return length


T = 10
for _ in range(T):
    tc = int(input())
    N = 100

    ladder = [input().split() for _ in range(N)]

    # 최단 경로를 저장할 변수
    min_length = float('inf')
    start_point = None

    # 출발점을 찾고
    for i in range(N):
        if ladder[0][i] == '1':
            # 경로의 길이를 계산하여
            current_length = calculate_length(ladder, i)
            # 최단 경로일 경우, 갱신
            if current_length <= min_length:
                min_length = current_length
                start_point = i

    print(f"#{tc} {start_point}")
