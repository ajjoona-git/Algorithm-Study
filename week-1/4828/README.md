# 4828: min max | D2

## 문제 출처
[SWEA](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZgvQCv6GNXHBIT9&contestProbId=AWTLQZwKon4DFAVT&probBoxId=AZgvQCv6GNbHBIT9&type=PROBLEM&problemBoxTitle=7%EC%9B%94&problemBoxCnt=19)

## 💡 접근 방식

### 1. 사용 알고리즘
* Python 내장 함수 `max()`와 `min()` 활용

### 2. 문제 풀이 과정
1. 각 테스트 케이스마다 `N`과 공백으로 구분된 숫자들을 리스트로 입력받습니다. 이때 `map(int, input().split())`을 사용하여 문자열을 정수 리스트로 변환합니다.

2. Python의 내장 함수인 `max()`와 `min()`을 사용하여 리스트의 최댓값과 최솟값을 각각 구합니다.

3. 구해진 최댓값에서 최솟값을 뺀 결과를 `result` 변수에 저장합니다.

4. 테스트 케이스 번호와 함께 `result` 값을 출력 형식에 맞춰 출력합니다.

---

## 💻 코드
* [4828.py](4828.py)