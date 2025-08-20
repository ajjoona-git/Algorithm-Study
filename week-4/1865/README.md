# 1865. 동철이의 일 분배 | D4

## 문제 출처
[SWEA](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZh9Pr4Kw1nHBINp&contestProbId=AV5LuHfqDz8DFAXc&probBoxId=AZh-M3iq4UfHBINp&type=PROBLEM&problemBoxTitle=Stack&problemBoxCnt=16)

## 💡 접근 방식

### 1. 사용 알고리즘
* **깊이 우선 탐색(DFS, Depth-First Search)**
* **재귀(Recursion)**와 **백트래킹(Backtracking)**

### 2. 문제 풀이 과정
1.  먼저 테스트 케이스의 개수 `T`를 입력받고, 각 테스트 케이스마다 직원의 수 `N`과 `N x N` 크기의 확률 배열 `P`를 입력받습니다.
2.  이 문제는 `N`명의 직원에게 `N`개의 일을 하나씩 할당하여 모든 일이 성공할 확률의 최댓값을 구해야 하므로, **모든 경우의 수를 탐색하는 백트래킹** 알고리즘을 사용합니다.
3.  탐색을 위한 재귀 함수 `get_percent(i, percent)`를 정의합니다. `i`는 현재 순서에서 일을 할당할 직원의 인덱스, `percent`는 현재까지의 성공 확률을 의미합니다.
4.  `max_percent` 변수를 `0`으로 초기화하여 최대 확률을 저장하고, `allocated` 배열을 `False`로 초기화하여 각 일이 할당되었는지 여부를 기록합니다.
5.  **가지치기(Pruning)**를 통해 불필요한 탐색을 줄입니다. 현재까지의 확률(`percent`)이 이미 `max_percent`보다 작거나 같으면, 더 이상 탐색해도 최댓값을 찾을 수 없으므로 `return`하여 탐색을 중단합니다.
6.  `i == N`이 되면 모든 직원에게 일이 할당된 것이므로, 현재의 `percent`와 `max_percent`를 비교하여 `max_percent`를 갱신합니다.
7.  `i`번 직원에게 `j`번 일을 할당하는 `for` 반복문을 사용합니다. `j`번 일이 아직 할당되지 않았다면, `allocated[j] = True`로 표시하고 `percent * P[i][j] * 0.01`을 계산하여 재귀 호출을 진행합니다.
8.  재귀 호출이 끝난 후에는 `allocated[j] = False`로 되돌려(백트래킹) 다른 직원에게 `j`번 일을 할당할 수 있도록 합니다.
9.  초기 호출은 `get_percent(0, 1)`로 시작하고, 모든 탐색이 끝나면 `max_percent`에 저장된 최종 확률을 출력 형식에 맞춰 출력합니다.


---

## 💻 코드
* [1865.py](1865.py)