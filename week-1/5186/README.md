# 5186: 이진수2 | D2

## 문제 출처
[SWEA](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZgvQCv6GNXHBIT9&contestProbId=AWTtj7GqeAgDFAVT&probBoxId=AZgvQCv6GNbHBIT9&type=PROBLEM&problemBoxTitle=7%EC%9B%94&problemBoxCnt=19)

## 💡 접근 방식

### 1. 사용 알고리즘
* **구현(Implementation)**
* **진법 변환**

### 2. 문제 풀이 과정
1.  먼저 테스트 케이스의 개수 `T`를 입력받습니다.
2.  이 문제는 10진수 소수를 2진수 소수로 변환하는 원리를 구현해야 합니다. 10진수 소수에 2를 곱하여 정수 부분을 취하고, 남은 소수 부분을 다시 2로 곱하는 과정을 반복합니다.
3.  각 테스트 케이스마다 0보다 크고 1미만인 십진수 `N`을 **float** 형태로 입력받습니다.
4.  변환된 2진수를 저장할 리스트 `binary`를 준비하고, 최대 13자리까지 변환을 시도하는 반복문을 실행합니다.
5.  매 반복마다 `N`에 2를 곱하고, 그 결과가 1 이상이면 이진수의 현재 자리가 `1`이고, `N`에서 1을 뺀 값으로 `N`을 갱신합니다.
6.  결과가 1 미만이면 현재 자리가 `0`이고, `N`은 그대로 둡니다.
7.  이 과정을 반복하다가 `N`이 `0`이 되면 변환이 완료된 것이므로 반복문을 `break`합니다.
8.  만약 12번의 반복이 끝난 후에도 `N`이 `0`이 아니라면, 12자리 이내로 변환이 불가능하므로 `'overflow'`를 출력합니다.
9.  변환이 완료된 경우, `binary` 리스트에 저장된 숫자들을 `map(str, binary)`로 문자열로 변환한 후 `"".join()`으로 합쳐서 출력 형식에 맞춰 출력합니다.

---

## 💻 코드
* [5186.py](5186.py)