# 258711. 도넛과 막대 그래프
"""
0. 생성 정점 찾기
    - 진입 차수는 0, 진출 차수는 2 이상인 정점

* 그래프를 대표하는 점 하나만 알아도 그래프의 개수를 구할 수 있다!
1. 도넛
    - 생성 정점의 총 진출 차수(전체 그래프 개수)에서 막대와 8자 모양 그래프의 개수를 제외

2. 막대
    - 진출 차수가 0인 정점은 막대 그래프의 끝

3. 8자
    - 진입 차수와 진출 차수가 2인 정점이 8자 모양 그래프의 중앙점
"""

def solution(edges):
    # 각 정점의 진입/진출 차수를 계산 {node: [in, out]}
    in_out_degrees = {}
    for u, v in edges:
        in_out_degrees.setdefault(u, [0, 0])[1] += 1
        in_out_degrees.setdefault(v, [0, 0])[0] += 1
            
    answer = [0] * 4  # [생성 정점, 도넛, 막대, 8자]

    for node, [in_degree, out_degree] in in_out_degrees.items():
        # 생성 정점 찾기
        if out_degree >= 2 and in_degree == 0:
            answer[0] = node
            num_graphs = in_out_degrees[node][1]
        
        # 막대 모양 그래프
        elif out_degree == 0 and in_degree > 0:
            answer[2] += 1

        # 8자 모양 그래프
        elif out_degree == 2 and in_degree >= 2:
            answer[3] += 1
    
    # 도넛 모양 그래프
    answer[1] = num_graphs - answer[2] - answer[3]
        
    return answer

print(solution([[2, 3], [4, 3], [1, 1], [2, 1]]))
print(solution([[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]))