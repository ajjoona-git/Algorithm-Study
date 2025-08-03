# 4834: 숫자 카드 | D2

## 문제 출처
[SWEA](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZgvQCv6GNXHBIT9&contestProbId=AWTLVouKpUgDFAVT&probBoxId=AZgvQCv6GNbHBIT9&type=PROBLEM&problemBoxTitle=7%EC%9B%94&problemBoxCnt=19)

## 💡 접근 방식

### 1. 사용 알고리즘
* **구현(Implementation)**
* **배열(Array)**을 활용한 빈도수 계산

### 2. 문제 풀이 과정
1.  먼저 테스트 케이스의 개수 `T`를 입력받고, 각 테스트 케이스를 순회합니다.
2.  각 테스트 케이스마다 카드 장수 `N`과 공백 없이 이어진 카드 숫자들을 문자열 형태로 입력받습니다.
3.  0부터 9까지의 숫자가 몇 번 나왔는지 기록하기 위해 길이가 10인 리스트 `card_list`를 0으로 초기화하여 생성합니다. `card_list`의 인덱스는 카드에 적힌 숫자를, 값은 해당 숫자의 빈도수를 의미합니다.
4.  입력받은 카드 문자열을 순회하며 각 문자를 정수로 변환한 뒤, 해당 숫자에 해당하는 `card_list`의 인덱스 값을 1씩 증가시켜 빈도수를 기록합니다.
5.  최빈수와 그 개수를 찾기 위해 `max_count_number`와 `max_count` 변수를 초기화합니다.
6.  `card_list`를 가장 큰 숫자(인덱스)부터 작은 숫자(인덱스) 순으로 순회합니다(9부터 0까지).
7.  만약 현재 숫자의 빈도수가 `max_count`보다 크다면, `max_count_number`를 현재 숫자로, `max_count`를 현재 빈도수로 갱신합니다.
8.  `max_count`보다 큰 빈도수를 가진 숫자를 먼저 발견하는 경우, 문제의 조건(빈도수가 같을 때는 숫자가 큰 쪽을 출력)을 자동으로 만족하게 됩니다.
9.  반복문이 끝나면 최종적으로 `max_count_number`와 `max_count`를 출력 형식에 맞춰 출력합니다.


---

## 💻 코드
* [4834.py](4834.py)