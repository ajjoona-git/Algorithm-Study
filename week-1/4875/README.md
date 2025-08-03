# 4875: 미로 | D2

## 문제 출처
[SWEA](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZgvQCv6GNXHBIT9&contestProbId=AWTQeET6QlADFAVT&probBoxId=AZgvQCv6GNbHBIT9&type=PROBLEM&problemBoxTitle=7%EC%9B%94&problemBoxCnt=19)

## 💡 접근 방식

### 1. 사용 알고리즘
* **깊이 우선 탐색(DFS, Depth-First Search)**
* **재귀(Recursion)** 또는 **스택(Stack)**을 활용한 탐색

### 2. 문제 풀이 과정
1.  먼저 미로를 2차원 배열 형태로 입력받아 저장합니다.
2.  탐색을 시작할 출발점 `'2'`의 좌표를 찾습니다.
3.  깊이 우선 탐색(DFS)을 사용하여 미로의 경로를 탐색합니다. DFS는 다음과 같은 방식으로 구현할 수 있습니다.
    * **재귀 함수**: 현재 위치에서 상하좌우를 탐색하며 갈 수 있는 길이 있다면 해당 위치로 이동하여 함수를 재귀적으로 호출합니다.
    * **스택(Stack)**: 탐색할 경로를 스택에 쌓고, 스택에서 하나씩 꺼내면서 경로를 탐색합니다.
4.  이미 방문한 위치를 다시 방문하지 않도록 `visited` 배열을 사용하여 경로를 추적합니다.
5.  탐색 중 도착점 `'3'`을 만나면 경로가 존재하는 것이므로 탐색을 종료하고 `1`을 반환합니다.
6.  만약 모든 경로를 탐색했음에도 `'3'`을 찾지 못하고 더 이상 갈 곳이 없다면, 경로가 존재하지 않는 것이므로 `0`을 반환합니다.
7.  최종 결과를 테스트 케이스 번호와 함께 출력합니다.


---

## 💻 코드
* [4875_recursive.py](4875_recursive.py)
* [4875_stack.py](4875_stack.py)