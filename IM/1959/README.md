# 1959: 두 개의 숫자열 | D2

## 문제 출처
[SWEA](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpoFaAS4DFAUq)

## 💡 접근 방식

### 1. 사용 알고리즘
* **구현(Implementation)**
* **슬라이딩 윈도우(Sliding Window)**

### 2. 문제 풀이 과정
1.  먼저 테스트 케이스의 개수 `T`를 입력받고, 각 테스트 케이스마다 두 숫자열의 길이 `N`, `M`과 두 숫자열 `a_list`, `b_list`를 입력받습니다.
2.  두 숫자열의 길이 `N`과 `M`을 비교하여 세 가지 경우로 나누어 처리합니다.
3.  `N < M`인 경우, 길이가 더 짧은 `a_list`를 `b_list` 위로 이동시키면서 곱의 합을 계산합니다.
4.  `N > M`인 경우, 길이가 더 짧은 `b_list`를 `a_list` 위로 이동시키면서 곱의 합을 계산합니다.
5.  `N == M`인 경우, 한 번만 곱의 합을 계산합니다.
6.  각 경우에 대해, 모든 가능한 위치에서의 곱의 합(`total`)을 구하고, 이 값들 중 최대값(`max_sum`)을 갱신합니다.
7.  모든 계산이 끝나면, `max_sum`에 저장된 최종 값을 출력 형식에 맞춰 출력합니다.

---

## 💻 코드
* [1959.py](1959.py)