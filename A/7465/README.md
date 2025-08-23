# 7465. 창용 마을 무리의 개수 | D4

## 문제 출처
![SWEA](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZgvQCv6GNXHBIT9&contestProbId=AWngfZVa9XwDFAQU&probBoxId=AZiiM-4KAVbHBIT9&type=PROBLEM&problemBoxTitle=A%ED%98%95_%EC%B6%94%EC%B2%9C+%ED%95%99%EC%8A%B5+%EC%9E%90%EB%A3%8C&problemBoxCnt=24)

## 💡 접근 방식

### 1. 사용 알고리즘
* **그래프 (Graph)**
* **깊이 우선 탐색 (DFS, Depth-First Search)**
* **연결 요소 (Connected Components)**

### 2. 문제 풀이 과정
1.  **문제 모델링**: 창용 마을의 사람들을 정점(Vertex)으로, 서로 아는 관계를 간선(Edge)으로 하는 **무방향 그래프(Undirected Graph)**로 문제를 모델링합니다. 여기서 '무리의 개수'는 그래프의 **연결 요소(Connected Component)의 개수**를 찾는 것과 같습니다.
2.  **그래프 표현**: 사람 간의 관계는 상호적(`A`가 `B`를 알면 `B`도 `A`를 안다)이므로, 인접 행렬(`town`)을 사용하여 `town[v1][v2]`와 `town[v2][v1]`을 모두 1로 설정하여 관계를 저장합니다.
3.  **전체 로직**:
    * 아직 무리에 포함되지 않은 모든 사람을 `people` 리스트에 넣어 관리합니다.
    * `people` 리스트가 빌 때까지 다음 과정을 반복합니다.
        1.  아직 무리가 정해지지 않은 사람이 남아있다는 의미이므로, 새로운 무리를 찾기 시작하고 `group` 카운트를 1 증가시킵니다.
        2.  `people` 리스트에서 임의의 사람 한 명을 꺼내, 그 사람을 시작점으로 DFS 탐색을 수행합니다.
4.  **DFS 탐색을 통한 무리 식별**:
    * `dfs(node)` 함수는 한 명(`node`)을 입력받아, 그 사람과 직간접적으로 연결된 모든 사람(하나의 무리)을 찾아냅니다.
    * 스택을 이용한 DFS를 통해 연결된 사람들을 계속 탐색해 나갑니다.
    * 탐색 과정에서 발견되는 사람은 **하나의 무리에 속하므로**, `people` 리스트에서 즉시 제거합니다.
    * `dfs` 함수가 종료되면, 시작점이었던 사람이 속한 무리의 모든 구성원이 `people` 리스트에서 제거된 상태가 됩니다.
5.  **결과 도출**: `people` 리스트가 모두 비워지면, `while`문이 종료됩니다. 이때 `group` 변수에 저장된 값이 바로 전체 무리의 개수가 됩니다.

---

## 💻 코드
* [7465.py](7465.py)