# 7465. 창용 마을 무리의 개수

# import sys
# sys.stdin = open("s_input.txt")


def dfs(node):
    """노드 번호 받아서 관계되어 있는 사람들은 people에서 remove"""
    stack = [node]
    
    while stack:
        curr = stack.pop()
        for i in range(N+1):
            # curr과 관계되어 있는 사람(1)
            if town[curr][i] == 1 and i in people:
                stack.append(i)
                people.remove(i)


T = int(input())
for tc in range(1,T+1):
    # N: num of people, M: num of edges
    N, M = map(int, input().split())
    
    # 마을 사람들의 관계 정보
    town = [[0] * (N+1) for _ in range(N+1)]
    for i in range(M):
        v1, v2 = map(int, input().split())
        town[v1][v2] = 1
        town[v2][v1] = 1
    
    people = list(range(1, N+1))
    group = 0

    # 그래프에서 사이클의 수 구하기
    # people이 비어있을 때까지 반복
    while people:
        dfs(people.pop())
        group += 1
    
    print(f"#{tc} {group}")