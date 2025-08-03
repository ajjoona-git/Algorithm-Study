T = int(input())  # 테스트 케이스의 수


def search(maze, x, y):
    '''
    주어진 2차원 리스트(maze)에서 (x,y)를 시작 위치로 하여
    탐색을 진행할 때, 길이 있다면 1을, 길이 없다면 0을 반환한다.

    dfs를 재귀함수로 구현했다.
    '''
    global result, visited
    # 현재 위치의 상하좌우를 탐색할 때 사용할 리스트
    explore = [(-1,0), (1,0), (0,-1), (0,1)]
    
    # visited에 현재 위치를 True로 바꾼다.
    visited[x][y] = True
    # print(visited)
    
    # 현재 위치에서 상하좌우의 길을 탐색한다.
    for dx, dy in explore:
        # 현재 위치가 지도 안에 있고, 방문하지 않은 곳이라면
        if 0 <= x+dx < N and 0 <= y+dy < N and not visited[x+dx][y+dy]:
            # 도착(3): 1 출력 후 종료
            if maze[x+dx][y+dy] == '3':
                result = 1
                return
            # 통로(0): 현재 위치를 갱신한다.
            elif maze[x+dx][y+dy] == '0':
                search(maze, x+dx, y+dy)



for test_case in range(1, T+1):
    N = int(input())  # 미로의 크기
    maze = []  # 미로를 저장할 2차원 리스트
    for _ in range(N):
        maze.append([i for i in input()])

    # 탐색 결과를 담을 변수 초기화
    result = 0

    # 방문 여부를 담을 2차원 리스트
    visited = [[False] * N for _ in range(N)]

    # 현재 위치 초기화
    # 출발(2)을 찾는다.
    for x in range(N):
        try:
            y = maze[x].index('2')
            break
        except ValueError:
            continue

    # 탐색을 시작한다.
    search(maze, x, y)

    # 결과 출력
    print(f'#{test_case} {result}')