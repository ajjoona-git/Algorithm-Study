# 23795: 우주 괴물 | D1

## 문제 출처
[SWEA](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZgvQCv6GNXHBIT9&contestProbId=AZU7flp6n8XHBIRK&probBoxId=AZh3fFV6jffHBINp&type=USER&problemBoxTitle=8%EC%9B%94+2%EC%A3%BC%EC%B0%A8%288%EC%9B%94+18%EC%9D%BC%EA%B9%8C%EC%A7%80+%ED%91%B8%EC%8B%9C%EC%98%A4%29&problemBoxCnt=8)

## 💡 접근 방식

### 1. 사용 알고리즘
* **구현(Implementation)**
* **2차원 배열 순회** 및 **방향 벡터(Delta Array)**

### 2. 문제 풀이 과정
1.  먼저 테스트 케이스의 개수 `T`를 입력받고, 각 테스트 케이스마다 배열의 크기 `N`과 `N x N` 크기의 2차원 배열 `grid`를 입력받습니다.
2.  `grid` 배열을 순회하여 우주 괴물의 위치(`'2'`)를 찾아 `monster` 변수에 저장합니다.
3.  광선이 발사되는 4방향(상하좌우)을 탐색하기 위해 `dr`과 `dc` 델타 배열을 정의합니다.
4.  `for` 반복문을 사용하여 4가지 방향을 순회하며 괴물의 광선 범위를 계산합니다.
5.  각 방향에 대해 `for step in range(1, N)` 반복문을 사용하여 `1`칸부터 `N`칸까지 거리를 확장하며 탐색합니다.
6.  탐색 중 배열의 경계를 벗어나거나 벽(`'1'`)을 만나면 해당 방향의 탐색을 중단하고 `break`를 통해 반복문을 종료합니다.
7.  빈 공간(`'0'`)을 발견하면, 해당 공간을 광선이 닿는 구역으로 표시하기 위해 `grid`의 해당 위치 값을 `'2'`로 변경합니다.
8.  괴물의 모든 광선 범위 계산이 끝나면, `grid` 배열을 다시 순회하여 값이 `'0'`인(즉, 광선이 닿지 않는) 공간의 개수를 셉니다.
9.  `safety_zone` 변수에 안전지대의 개수를 누적하여 저장합니다.
10. 최종적으로 계산된 `safety_zone` 값을 출력 형식에 맞춰 출력합니다.

---

## 💻 코드
* [23795.py](23795.py)