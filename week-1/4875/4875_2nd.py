# 4875. 미로

def escape_maze(map, r, c, N):
    """(r, c)부터 출발해서 미로를 탈출하는 길을 찾는 함수"""
    # 인접한 요소를 탐색하기 위한 델타 배열 (상하좌우 순)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    # 방문 여부를 표시하기 위한 리스트
    visited = [[False] * N for _ in range(N)]
    
    # 현재 탐색 중인 경로
    stack = [(r, c)]
    visited[r][c] = True
    
    # stack에 값이 남아있을 때까지
    while stack:
        # 현재 위치를 스택에서 꺼내 탐색 시작
        r, c = stack.pop()

        # 현재 위치에서 인접한 4방향(상하좌우)을 모두 탐색
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            # 미로의 범위를 벗어나지 않으면서 방문하지 않았을 경우
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                # 도착이면 탐색 종료
                if map[nr][nc] == '3':
                    return 1
                # 통로라면 스택에 추가하고 방문 처리
                elif map[nr][nc] == '0':
                    visited[nr][nc] = True
                    stack.append((nr, nc))
                    # print(stack[-1])
                # 벽이거나 출발지라면 변화 없음
                # else:
                #     continue
    return 0


T = int(input())  # 테스트 케이스의 수
for tc in range(1, T+1):
    N = int(input())  # 미로의 크기
    maze = [list(input()) for _ in range(N)]  # 미로를 리스트로 변환

    # 출발 위치 설정
    start_r, start_c = -1, -1
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                start_r, start_c = i, j
                break
        if start_r != -1:
            break
    
    result = escape_maze(maze, start_r, start_c, N)  # 탐색 결과
    
    print(f'#{tc} {result}')