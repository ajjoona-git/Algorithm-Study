# 1926: 간단한 369게임 | D2

## 문제 출처
[SWEA](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZgvQCv6GNXHBIT9&contestProbId=AV5PTeo6AHUDFAUq&probBoxId=AZhi468aVsDHBINp&type=PROBLEM&problemBoxTitle=8%EC%9B%94+1%EC%A3%BC%EC%B0%A8%288%2F7%EA%B9%8C%EC%A7%80+%ED%91%B8%EC%8B%9C%EC%98%A4%29&problemBoxCnt=5)

## 💡 접근 방식

### 1. 사용 알고리즘
* **구현(Implementation)**
* **문자열 처리**

### 2. 문제 풀이 과정
1.  먼저 `1`부터 `N`까지의 숫자를 순회하는 `for` 반복문을 사용합니다.
2.  각 숫자 `i`를 문자열로 변환하여 `i_str`에 저장합니다. 이는 `replace()` 메소드를 사용하기 위함입니다.
3.  `i_str`에 `3`, `6`, `9`가 포함되어 있으면 각각 `'-'`로 치환합니다.
4.  치환 후 `i_str`에 `'-'`가 포함되어 있는지 확인합니다.
5.  `'-'`가 포함되어 있다면, `split('-')`를 사용하여 `-`를 기준으로 문자열을 분리합니다. 이 때 생성되는 리스트의 길이는 `-`의 개수 + 1이 됩니다.
6.  `len(i_str.split('-')) - 1`로 `-`의 개수를 구하고, 그 개수만큼 `-`를 반복하여 새로운 `i_str`을 만듭니다.
7.  만약 `'-'`가 포함되어 있지 않다면, `i_str`은 원래 숫자를 그대로 유지합니다.
8.  각 `i`에 대한 처리가 끝나면, 결과를 공백으로 구분하여 한 줄에 출력합니다.

---

## 💻 코드
* [1926.py](1926.py)