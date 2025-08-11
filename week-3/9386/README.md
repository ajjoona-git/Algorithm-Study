# 9386. 연속한 1의 개수 | D1

## 문제 출처
[SWEA](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZgvQCv6GNXHBIT9&contestProbId=AXALDUIq97oDFASI&probBoxId=AZh3fFV6jffHBINp&type=USER&problemBoxTitle=8%EC%9B%94+2%EC%A3%BC%EC%B0%A8%288%EC%9B%94+13%EC%9D%BC%EA%B9%8C%EC%A7%80+%ED%91%B8%EC%8B%9C%EC%98%A4%29&problemBoxCnt=8)

## 💡 접근 방식

### 1. 사용 알고리즘
* **구현(Implementation)**
* **반복문** 및 **상태 관리**

### 2. 문제 풀이 과정
1.  먼저 테스트 케이스의 개수 `T`를 입력받고, 각 테스트 케이스마다 수열의 길이 `N`과 0과 1로 구성된 수열 `arr`를 입력받습니다.
2.  연속된 1의 개수를 셀 `count`와 그 중 최대값을 저장할 `max_count` 변수를 `0`으로 초기화합니다.
3.  수열 `arr`를 순회하면서 각 문자가 `1`인지 `0`인지 확인합니다.
4.  만약 현재 문자가 `1`이면 `count`를 1 증가시켜 연속된 1의 개수를 카운트합니다. 또한, 현재 `count`가 `max_count`보다 크다면 `max_count`를 갱신합니다.
5.  현재 문자가 `0`이면, 연속된 1의 개수가 끊겼다는 뜻이므로 `count`를 `0`으로 초기화합니다.
6.  `for` 반복문이 끝난 후, `max_count`에 저장된 값이 연속된 1의 최대 개수가 됩니다.
7.  최종적으로 `max_count`에 저장된 값을 출력 형식에 맞춰 출력합니다.

---

## 💻 코드
* [9386.py](9386.py)