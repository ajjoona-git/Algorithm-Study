# 20397: 돌 뒤집기 게임 2 | D1


## 문제 출처
[SWEA](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZgvQCv6GNXHBIT9&contestProbId=AY3o7m4axawDFAUZ&probBoxId=AZh3fFV6jffHBINp&type=USER&problemBoxTitle=8%EC%9B%94+2%EC%A3%BC%EC%B0%A8%288%EC%9B%94+18%EC%9D%BC%EA%B9%8C%EC%A7%80+%ED%91%B8%EC%8B%9C%EC%98%A4%29&problemBoxCnt=8)

## 💡 접근 방식

### 1. 사용 알고리즘
* **구현(Implementation)**
* **배열 순회** 및 **조건문**

### 2. 문제 풀이 과정
1.  먼저 테스트 케이스의 개수 `T`를 입력받고, 각 테스트 케이스마다 돌의 수 `N`과 뒤집기 횟수 `M`을 입력받습니다.
2.  돌의 초기 상태를 담은 리스트 `stones`를 입력받습니다.
3.  `for _ in range(M)` 반복문을 통해 뒤집기 과정을 `M`번 반복합니다.
4.  각 뒤집기 과정마다 돌을 뒤집을 기준 인덱스 `i`와 마주보는 돌의 개수 `j`를 입력받습니다.
5.  `for step in range(1, j+1)` 반복문을 통해 `j`개의 돌에 대해 마주보는 돌의 인덱스 `idx_l`과 `idx_r`을 계산합니다.
6.  `if` 조건문을 통해 계산된 인덱스가 배열의 범위를 벗어나지 않는지 확인합니다. 범위를 벗어나면 `break`를 통해 반복문을 종료합니다.
7.  두 마주보는 돌의 색깔(`'0'` 또는 `'1'`)이 같은지 확인합니다.
    * 색깔이 같으면 두 돌의 색깔을 뒤집습니다.
    * 색깔이 다르면 그대로 둡니다.
8.  `M`번의 뒤집기 과정이 모두 끝나면, 최종적으로 `stones` 리스트에 저장된 돌의 상태를 출력 형식에 맞춰 출력합니다.

---

## 💻 코드
* [20397.py](20397.py)