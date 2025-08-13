# 20230: 풍선팡 보너스 게임 2 | D2

## 문제 출처
[SWEA](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZgvQCv6GNXHBIT9&contestProbId=AY3FFOTaN7EDFAXh&probBoxId=AZh3fFV6jffHBINp&type=USER&problemBoxTitle=8%EC%9B%94+2%EC%A3%BC%EC%B0%A8%288%EC%9B%94+18%EC%9D%BC%EA%B9%8C%EC%A7%80+%ED%91%B8%EC%8B%9C%EC%98%A4%29&problemBoxCnt=8)

## 💡 접근 방식 1: 델타

### 1. 사용 알고리즘
* **구현(Implementation)**
* **2차원 배열 순회** 및 **방향 벡터(Delta Array)**

### 2. 문제 풀이 과정
1.  먼저 테스트 케이스의 개수 `T`를 입력받고, 각 테스트 케이스마다 배열의 크기 `N`과 `N x N` 크기의 2차원 배열 `grid`를 입력받습니다.
2.  상하좌우 4방향을 탐색하기 위한 델타 배열 `dr`과 `dc`를 정의합니다.
3.  `max_score` 변수를 `0`으로 초기화하여 최대 점수를 저장합니다.
4.  이중 반복문을 사용하여 배열 `grid`의 모든 위치 `(r, c)`를 순회하며 각 풍선의 위치를 중심으로 폭발 범위를 계산합니다.
5.  `current_score` 변수에 현재 위치의 점수 `grid[r][c]`를 초기값으로 저장합니다.
6.  `for i in range(4)` 반복문을 통해 4가지 방향(상하좌우)을 순회하며 폭발 범위를 계산합니다.
7.  각 방향에 대해 `for k in range(1, N)` 반복문을 사용하여 거리를 `1`부터 `N-1`까지 확장하며 탐색합니다.
8.  다음 위치 `(nr, nc)`가 배열의 경계 내부에 있는지 확인하고, 경계 내부에 있다면 `current_score`에 해당 위치의 점수를 더합니다.
9.  경계를 벗어나면 `break`를 통해 해당 방향의 탐색을 중단하고 다음 방향으로 넘어갑니다.
10. `current_score`와 `max_score`를 비교하여 `max_score`를 갱신합니다.
11. 모든 풍선에 대한 계산이 끝나면, `max_score`에 저장된 최종 값을 출력 형식에 맞춰 출력합니다.


---

## 💻 코드
* [20230.py](20230.py)