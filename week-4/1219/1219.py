# 1219. 길찾기

# import sys
# sys.stdin = open("input (1).txt")


def dfs(start):
    # 스택 초기화
    stack = [start]
    visited = [0] * 100

    while stack:
        current = stack.pop()
        # 도착지(B도시, 인덱스 99)라면 1 반환
        if current == 99:
            return 1
        
        # 방문한 적 없는 노드일 경우
        if visited[current] == 0:
            visited[current] = 1
            # 연결된 길을 찾는다. 
            for next_node in range(99, 0, -1):
                if adj_lst[current][next_node] == 1 and visited[next_node] == 0:
                    stack.append(next_node)

    # 도착지에 도달하지 못했다면 0 반환
    return 0


T = 10
for _ in range(T):
    # N: 길의 총 개수(간선의 수)
    tc, N = map(int, input().split())
    edge = list(map(int, input().split()))

    # A도시(출발지)는 인덱스 0, B도시(도착지)는 인덱스 99
    adj_lst = [[0] * 100 for _ in range(100)]
    for i in range(N):
        v_from, v_to = edge[i*2], edge[i*2 + 1]
        adj_lst[v_from][v_to] = 1

    # 출발지(A도시, 인덱스 0)부터 dfs
    result = dfs(0)
    print(f'#{tc} {result}')