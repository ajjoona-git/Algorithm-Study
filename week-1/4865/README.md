# 4865: 글자수 | D2

## 문제 출처
[SWEA](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZgvQCv6GNXHBIT9&contestProbId=AWTQSs6qQL0DFAVT&probBoxId=AZgvQCv6GNbHBIT9&type=PROBLEM&problemBoxTitle=7%EC%9B%94&problemBoxCnt=19)

## 💡 접근 방식

### 1. 사용 알고리즘
* **딕셔너리(Dictionary)**를 활용한 빈도수 계산
* **문자열 메소드 `count()`**

### 2. 문제 풀이 과정
1.  먼저 테스트 케이스의 개수 `T`를 입력받습니다.
2.  각 테스트 케이스마다 두 개의 문자열 `str1`과 `str2`를 입력받습니다.
3.  `str1`에 포함된 각 문자가 `str2`에 몇 번 등장하는지 그 횟수를 세기 위해 **딕셔너리**를 사용합니다.
4.  `max_count` 변수를 `0`으로 초기화하여 가장 많은 글자의 개수를 저장할 준비를 합니다.
5.  `str1`을 순회하면서 각 문자 `char`를 가져옵니다.
6.  `str2`에서 `char`의 등장 횟수를 `str2.count(char)` 메소드를 사용하여 계산합니다.
7.  계산된 횟수가 현재 `max_count`보다 크다면, `max_count`를 이 횟수로 갱신합니다.
8.  `str1`의 모든 문자에 대한 순회가 끝나면, `max_count`에는 가장 많은 글자의 개수가 저장됩니다.
9.  테스트 케이스 번호와 함께 `max_count` 값을 출력 형식에 맞춰 출력합니다.


---

## 💻 코드
* [4865.py](4865.py)