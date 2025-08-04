# 1859: 백만 장자 프로젝트 | D2

## 문제 출처
[SWEA](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZgvQCv6GNXHBIT9&contestProbId=AV5LrsUaDxcDFAXc&probBoxId=AZhi468aVsDHBINp&type=PROBLEM&problemBoxTitle=8%EC%9B%94+1%EC%A3%BC%EC%B0%A8%288%2F7%EA%B9%8C%EC%A7%80+%ED%91%B8%EC%8B%9C%EC%98%A4%29&problemBoxCnt=5)

## 💡 접근 방식

### 1. 사용 알고리즘
* **구현(Implementation)**
* **그리디(Greedy)** 알고리즘
* **배열 순회(Array Traversal)**

### 2. 문제 풀이 과정
1.  먼저 테스트 케이스의 개수 `T`를 입력받고, 각 테스트 케이스마다 기간 `N`과 N일 간의 매매가를 담은 리스트 `prices`를 입력받습니다.
2.  이 문제는 **가장 높은 매매가에 물건을 팔아야** 이익을 최대화할 수 있다는 점에 착안하여 **그리디 알고리즘**을 적용할 수 있습니다.
3.  탐색은 매매가 리스트의 **마지막 날부터 역순**으로 진행합니다. 마지막 날의 매매가를 현재까지의 `max_price`로 초기화하고, 최대 이익을 저장할 `profit` 변수를 `0`으로 초기화합니다.
4.  마지막 날부터 첫날까지 거꾸로 리스트를 순회합니다.
5.  현재 날짜의 매매가(`prices[i]`)가 현재까지의 `max_price`보다 크다면, 이는 미래의 가장 높은 매매가이므로 `max_price`를 현재 매매가로 갱신합니다.
6.  만약 현재 날짜의 매매가가 `max_price`보다 작거나 같다면, 현재 물건을 구매하고 미래에 `max_price`에 팔 수 있으므로, `(max_price - prices[i])`만큼 이익을 `profit`에 더합니다.
7.  순회가 끝난 후, `profit`에 저장된 값이 최대 이익이 됩니다.
8.  최종 결과를 테스트 케이스 번호와 함께 출력 형식에 맞춰 출력합니다.

---

## 💻 코드
* [1859.py](1859.py)