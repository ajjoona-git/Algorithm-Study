# 5643. 키 순서 | D4

## 문제 출처
[SWEA](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZgvQCv6GNXHBIT9&contestProbId=AWXQsLWKd5cDFAUo&probBoxId=AZj5f5Z6YLLHBITM+&type=PROBLEM&problemBoxTitle=9%EC%9B%94+1-2%EC%A3%BC%EC%B0%A8%289%EC%9B%94+11%EC%9D%BC%EA%B9%8C%EC%A7%80+%ED%91%B8%EC%8B%9C%EC%98%A4%29&problemBoxCnt=++5+)

## 💡 접근 방식

### 1. 사용 알고리즘
* **그래프 (Graph)**
* **너비 우선 탐색 (BFS, Breadth-First Search)**
* **큐 (Queue)**

### 2. 문제 풀이 과정
1.  **문제 모델링**: 학생들의 키 비교 관계를 **방향 그래프(Directed Graph)**로 모델링합니다. `A`학생이 `B`학생보다 키가 작다는 관계를 `A -> B` 간선으로 표현합니다. 어떤 학생의 키 순서를 정확히 알 수 있다는 것은, **자신을 제외한 모든 학생(N-1명)과 키 대소 관계를 알 수 있다**는 의미입니다.
2.  **핵심 아이디어**: 학생 `X`의 순서를 알려면, `X`보다 키가 큰 학생들의 수와 `X`보다 키가 작은 학생들의 수의 합이 `N-1`이 되어야 합니다.
    * `X`보다 키가 큰 학생들: `X`에서 출발하여 도달할 수 있는 모든 노드.
    * `X`보다 키가 작은 학생들: `X`를 향해 들어오는 간선을 역으로 따라가 도달할 수 있는 모든 노드.
3.  **양방향 그래프 표현**: 위 두 종류의 학생 수를 효율적으로 찾기 위해, 두 개의 인접 리스트를 생성합니다.
    * **`taller`**: `A -> B` 관계를 그대로 저장합니다. `taller[A]`는 `A`보다 키가 큰 학생들의 목록입니다.
    * **`smaller`**: `A -> B` 관계를 `B -> A`로 뒤집어서 저장합니다. `smaller[B]`는 `B`보다 키가 작은 학생들의 목록입니다.
4.  **BFS를 이용한 관계 탐색 (`traverse` 함수)**:
    * `traverse(graph, node)` 함수는 주어진 그래프(`taller` 또는 `smaller`)와 시작 노드(`node`)를 받아, 너비 우선 탐색(BFS)을 수행합니다.
    * 이 함수는 `node`에서부터 도달 가능한 모든 노드의 개수를 세어 반환합니다.
5.  **결과 도출**:
    * 1번부터 N번까지 모든 학생을 순회합니다.
    * 각 학생(`student`)에 대해 다음을 계산합니다.
        * `traverse(taller, student)`: `student`보다 키가 큰 학생의 수
        * `traverse(smaller, student)`: `student`보다 키가 작은 학생의 수
    * 두 결과의 합이 `N-1`과 같다면, 해당 학생은 자신의 키 순서를 정확히 알 수 있으므로 `result`를 1 증가시킵니다.
    * 모든 학생에 대한 검사가 끝나면 `result`를 출력합니다.

---

## 💻 코드
* [5643.py](5643.py)