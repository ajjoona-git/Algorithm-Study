T = int(input())  # 테스트 케이스의 수

for test_case in range(1, T+1):
    V, E = map(int, input().split())  # 노드의 수 V와 간선의 수 E

    # 1. (V+1) * (V+1) 크기의 빈 리스트 graph를 생성한다.
    # 노드번호는 1번부터 존재하며, 노드번호와 인덱스번호를 일치시키기 위함.
    graph = [ [0] * (V+1) for _ in range(V+1) ]

    # 2. E개의 간선을 순회하면서(입력받으면서) 경로를 표시한다.
    for _ in range(E):
        i, j = map(int, input().split())
        graph[i][j] = 1

    S, G = map(int, input().split())  # 출발 노드 S와 도착노드 G

    # 3. S부터 시작해서 연결된 노드를 따라 간다.
    # 탐색에 필요한 변수 초기화
    result = 0
    i = S
    visited = [0]  # 거쳐온 노드를 담는 리스트

    # visited가 비어있는 경우 종료
    while visited:
        # 계속해서 탐색을 진행한다.
        try:
            j = graph[i].index(1)
        # 더 이상 진행할 경로가 없는 경우
        except ValueError:
            # 직전 노드로 돌아간다.
            i = visited.pop()
            # 0이 반환되면 모든 경로를 방문한 것이므로 탐색을 종료한다.
            if i == 0:
                break
        # 경로가 있는 경우
        else:
            # print(i,j)
            # G를 만나면, 1을 반환한다.
            if j == G:
                result = 1
                break
            # 방문한 노드는 다시 탐색하지 않기 위해 0으로 초기화한다.
            graph[i][j] = 0
            visited.append(i)
            i = j
        
    # 결과 출력
    print(f'#{test_case} {result}')