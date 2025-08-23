# 1219. 길찾기 | D4

## 문제 출처
![SWEA](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZh9Pr4Kw1nHBINp&contestProbId=AV14geLqABQCFAYD&probBoxId=AZh-M3iq4UfHBINp&type=PROBLEM&problemBoxTitle=Stack&problemBoxCnt=16)

## 💡 접근 방식

### 1. 사용 알고리즘
* **그래프 (Graph)**
* **깊이 우선 탐색 (DFS, Depth-First Search)**
* **스택 (Stack)**

### 2. 문제 풀이 과정
1.  **그래프 모델링**: 도시들을 정점(Vertex)으로, 단방향 길들을 간선(Edge)으로 하는 유향 그래프(Directed Graph)로 문제를 모델링합니다. 출발점은 0번, 도착점은 99번 정점입니다.
2.  **인접 행렬 사용**: 그래프의 연결 관계를 나타내기 위해 100x100 크기의 2차원 리스트(인접 행렬 `adj_lst`)를 사용합니다. `adj_lst[from][to] = 1`은 `from`에서 `to`로 가는 길이 존재함을 의미합니다.
3.  **경로 탐색 알고리즘 선택**: 출발점에서 도착점까지의 경로 존재 여부를 확인하기 위해 **깊이 우선 탐색(DFS)**을 사용합니다. DFS는 한 경로를 따라 최대한 깊게 탐색하므로 경로 찾기 문제에 적합합니다.
4.  **DFS 구현 (스택 사용)**:
    * 재귀 대신 스택(Stack)을 이용한 반복문 방식으로 DFS를 구현합니다.
    * `visited` 리스트를 두어 이미 방문한 정점은 다시 방문하지 않도록 하여 무한 루프를 방지합니다.
    * 스택에 시작점 `0`을 넣고 탐색을 시작합니다.
    * 스택이 비어있지 않은 동안 다음을 반복합니다:
        1.  스택에서 현재 정점(`current`)을 꺼냅니다.
        2.  `current`가 도착점(`99`)이면 경로를 찾은 것이므로 즉시 `1`을 반환하고 탐색을 종료합니다.
        3.  `current`를 방문한 적이 없다면, `visited`에 방문 표시를 합니다.
        4.  인접 행렬을 통해 `current`와 연결된 모든 다음 정점(`next_node`)을 찾습니다. 만약 `next_node`를 아직 방문하지 않았다면 스택에 추가합니다.
5.  **결과 반환**: 스택이 모두 비워질 때까지 `99`번 정점에 도달하지 못했다면, 이는 경로가 존재하지 않음을 의미하므로 `0`을 반환합니다.

---

## 💻 코드
* [1219.py](1219.py)