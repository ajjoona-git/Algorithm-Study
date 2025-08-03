# 4835: 구간합 | D2

## 문제 출처
[SWEA](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZgvQCv6GNXHBIT9&contestProbId=AWTLXCuapdcDFAVT&probBoxId=AZgvQCv6GNbHBIT9&type=PROBLEM&problemBoxTitle=7%EC%9B%94&problemBoxCnt=19)

## 💡 접근 방식

### 1. 사용 알고리즘
* **구현(Implementation)**
* **슬라이딩 윈도우(Sliding Window)** 개념 적용

### 2. 문제 풀이 과정
1.  먼저 테스트 케이스의 개수 `T`를 입력받습니다.
2.  각 테스트 케이스마다 정수의 개수 `N`과 구간의 개수 `M`을 입력받고, `N`개의 정수를 담은 리스트 `num_list`를 생성합니다.
3.  `N`개의 정수 리스트에서 이웃한 `M`개의 합을 모두 계산해야 합니다. 이를 위해 **슬라이딩 윈도우** 개념을 적용합니다. `num_list`의 인덱스 `0`부터 `N-M`까지 순회하는 바깥쪽 반복문을 사용합니다.
4.  각 구간의 합을 저장할 리스트 `sum_list`를 준비합니다.
5.  바깥쪽 반복문(`i`) 안에서, 현재 위치(`i`)부터 `M`개의 숫자를 더하는 안쪽 반복문(`j`)을 실행합니다. `num_list[i+j]`를 더해 `sub_total`을 계산합니다.
6.  안쪽 반복문이 끝나면 계산된 `sub_total`을 `sum_list`에 추가합니다.
7.  모든 구간의 합이 `sum_list`에 저장되면, Python의 내장 함수 `max()`와 `min()`을 사용하여 `sum_list`에서 최댓값과 최솟값을 찾습니다.
8.  `최댓값 - 최솟값`을 계산하여 `result`에 저장하고, 테스트 케이스 번호와 함께 출력 형식에 맞춰 출력합니다.



---

## 💻 코드
* [4835.py](4835.py)