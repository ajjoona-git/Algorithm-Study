# 258711. 도넛과 막대 그래프
# 38.1/100점 시간초과+오답
"""
1. 도넛 == 사이클
    - n개의 정점과 n개의 간선
    - 아무 한 정점에서 출발해 이용한 적 없는 간선을 계속 따라가면 나머지 n-1개의 정점들을 한 번씩 방문한 뒤 원래 출발했던 정점으로 돌아오게 됩니다.

2. 막대
    - n개의 정점과 n-1개의 간선
    - 간선을 계속 따라가면 나머지 n-1개의 정점을 한 번씩 방문하게 되는 정점이 단 하나 존재

3. 8자
    - 2n+1개의 정점과 2n+2개의 간선
    - 크기가 동일한 2개의 도넛 모양 그래프에서 정점을 하나씩 골라 결합시킨 형태
"""


def define_type(adj_dict, node):
    stack = [node]
    visited = {node}
    is_8 = False

    while stack:
        curr_node = stack.pop()
        
        for next_node in adj_dict.get(curr_node, []):
            if next_node not in visited:
                visited.add(next_node)
                stack.append(next_node)
            
            elif next_node == node:
                # 8자 모양
                if stack:
                    is_8 = True

                elif is_8:
                    return 3, visited
                
                # 도넛 모양
                else:
                    return 1, visited
            
            else:
                return -1, {node}
            
    # 막대 모양
    return 2, visited


def solution(edges):
    adj_dict = {}
    for u, v in edges:
        adj_dict.setdefault(u, []).append(v)

    num_nodes = max(adj_dict.keys())
    nodes = {i for i in range(1, num_nodes+1)}
    answer = [0] * 4

    for node in sorted(nodes, key=lambda x: len(adj_dict.get(x, [])), reverse=True):
        if node not in nodes:
            continue

        graph_type, visited = define_type(adj_dict, node)
        
        if graph_type == -1:
            answer[0] = node
            continue
        
        answer[graph_type] += 1
        nodes = nodes - visited

    return answer

print(solution([[2, 3], [4, 3], [1, 1], [2, 1]]))
print(solution([[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]))