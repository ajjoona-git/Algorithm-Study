# 2105. 디저트 카페

## 문제 출처
[SWEA](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZgvQCv6GNXHBIT9&contestProbId=AV5VwAr6APYDFAWu&probBoxId=AZjE2kOaAXDHBIO0&type=PROBLEM&problemBoxTitle=8%EC%9B%94+3-4%EC%A3%BC%EC%B0%A8%288%2F28%EA%B9%8C%EC%A7%80+%ED%91%B8%EC%8B%9C%EC%98%A4%29&problemBoxCnt=4)

## 💡 접근 방식

### 1. 사용 알고리즘
* **구현(Implementation)**
* **브루트포스(Brute-force)**
* **2차원 배열 순회** 및 **방향 벡터(Delta Array)**

### 2. 문제 풀이 과정
1.  먼저 테스트 케이스의 개수 `T`를 입력받고, 각 테스트 케이스마다 배열의 크기 `N`과 `N x N` 크기의 `cafe` 배열을 입력받습니다.
2.  이 문제는 모든 가능한 경로를 탐색하여 중복되지 않는 디저트를 가장 많이 먹을 수 있는 경로를 찾아야 하므로, **브루트포스** 탐색을 사용합니다.
3.  `for` 반복문을 사용하여 모든 가능한 시작 위치 `(r, c)`를 탐색하고, 각 시작점으로부터 모든 가능한 `width`와 `height`를 가진 마름모 모양의 경로를 시뮬레이션합니다.
4.  마름모 모양의 경로를 탐색하기 위해 시계 방향으로 4방향(우하, 좌하, 좌상, 우상)을 나타내는 델타 배열을 사용합니다.
5.  `current_desserts` 리스트에 현재 경로에서 먹은 디저트의 종류를 저장하여, 중복된 디저트가 있는지 확인합니다.
6.  탐색 중 중복된 디저트를 발견하면 해당 경로는 무효하므로 탐색을 중단하고 다른 경로를 시도합니다.
7.  경로가 성공적으로 시작점 `(r, c)`으로 돌아오면, 현재 경로의 길이(`len(current_desserts)`)와 `max_desserts`를 비교하여 더 긴 길이를 갱신합니다.
8.  모든 가능한 경로에 대한 탐색이 끝나면 `max_desserts`에 저장된 최종 값을 출력 형식에 맞춰 출력합니다.

---

## 💻 코드
* [2105.py](2105.py)