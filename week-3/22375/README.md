# 22375. 스위치 조작 | D1

## 문제 출처
[SWEA](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZgvQCv6GNXHBIT9&contestProbId=AZHA7Cn6ZgsDFAQP&probBoxId=AZh3fFV6jffHBINp&type=USER&problemBoxTitle=8%EC%9B%94+2%EC%A3%BC%EC%B0%A8%288%EC%9B%94+13%EC%9D%BC%EA%B9%8C%EC%A7%80+%ED%91%B8%EC%8B%9C%EC%98%A4%29&problemBoxCnt=8)

## 💡 접근 방식

### 1. 사용 알고리즘
* **구현(Implementation)**
* **그리디(Greedy)** 알고리즘

### 2. 문제 풀이 과정
1.  먼저 테스트 케이스의 개수 `T`를 입력받고, 각 테스트 케이스마다 스위치의 개수 `N`, 초기 상태 `switches`, 최종 상태 `final_status`를 입력받습니다.
2.  조작 횟수를 저장할 `count` 변수를 `0`으로 초기화합니다.
3.  `switches` 배열을 처음부터 끝까지 순회하며 현재 스위치 상태(`switches[i]`)와 최종 상태(`final_status[i]`)를 비교합니다.
4.  만약 두 상태가 다르다면, 현재 위치 `i`의 스위치를 조작해야 한다는 의미이므로 `count`를 1 증가시킵니다.
5.  스위치 조작은 현재 위치 `i`부터 배열의 끝까지 모든 스위치의 상태를 반전시키는 방식으로 진행됩니다. `(switches[j] + 1) % 2`를 사용하여 `0`은 `1`로, `1`은 `0`으로 바꿉니다.
6.  `for` 반복문이 끝나면 `switches` 배열은 `final_status`와 동일해지고, `count`에는 최소 조작 횟수가 저장됩니다.
7.  최종 결과를 테스트 케이스 번호와 함께 출력 형식에 맞춰 출력합니다.

---

## 💻 코드
* [22375.py](22375.py)