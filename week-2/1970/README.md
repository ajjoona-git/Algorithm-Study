# 1970: 쉬운 거스름돈 | D2

## 문제 출처
[SWEA](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZgvQCv6GNXHBIT9&contestProbId=AV5PsIl6AXIDFAUq&probBoxId=AZhi468aVsDHBINp&type=PROBLEM&problemBoxTitle=8%EC%9B%94+1%EC%A3%BC%EC%B0%A8%288%2F7%EA%B9%8C%EC%A7%80+%ED%91%B8%EC%8B%9C%EC%98%A4%29&problemBoxCnt=4)

## 💡 접근 방식

### 1. 사용 알고리즘
* **구현(Implementation)**
* **그리디(Greedy)** 알고리즘

### 2. 문제 풀이 과정
1.  먼저 테스트 케이스의 개수 `T`를 입력받고, 각 테스트 케이스마다 거슬러 주어야 할 금액 `N`을 입력받습니다.
2.  문제의 핵심은 가장 적은 수의 돈으로 거스름돈을 주는 것이므로, **가장 큰 단위의 돈부터** 차례로 계산하는 **그리디 알고리즘**을 사용합니다.
3.  돈의 종류를 담은 리스트 `moneys`와 각 돈의 개수를 저장할 `changes` 리스트를 준비합니다.
4.  `for` 반복문을 사용하여 `moneys` 리스트를 순회합니다.
5.  각 돈의 종류(`money`)에 대해 `N`을 `money`로 나눈 몫을 계산하여 `changes` 리스트의 해당 인덱스에 저장합니다.
6.  `N`을 `money`로 나눈 나머지를 계산하여 `N` 값을 갱신합니다. 이 과정을 통해 다음으로 작은 단위의 돈에 대한 계산을 이어서 진행할 수 있습니다.
7.  모든 돈의 종류에 대한 계산이 끝나면, 최종적으로 `changes` 리스트에 저장된 각 돈의 개수를 출력 형식에 맞춰 출력합니다.


---

## 💻 코드
* [1970.py](1970.py)