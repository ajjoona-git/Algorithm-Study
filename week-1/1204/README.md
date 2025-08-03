# 1204: 최빈수 구하기 | D2

## 문제 출처
[SWEA](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZgvQCv6GNXHBIT9&contestProbId=AV13zo1KAAACFAYh&probBoxId=AZgvQCv6GNbHBIT9&type=PROBLEM&problemBoxTitle=7%EC%9B%94&problemBoxCnt=19)

## 💡 접근 방식

### 1. 사용 알고리즘
* **딕셔너리(Dictionary)**를 활용한 빈도수 계산
* **반복문**을 통한 최댓값 찾기

### 2. 문제 풀이 과정
1.  학생들의 점수 리스트를 입력받습니다. 이 과정에서 `map(int, input().split())`을 사용하여 문자열 형태의 점수를 정수로 변환합니다.
2.  `딕셔너리`를 생성하여 점수(`key`)와 해당 점수의 빈도수(`value`)를 저장합니다.
3.  점수 리스트를 순회하며 딕셔너리에 점수가 이미 존재하면 빈도수를 1 증가시키고, 존재하지 않으면 새로운 항목으로 추가하며 빈도수를 1로 초기화합니다.
4.  모든 점수를 처리한 후, `딕셔너리.values()`에서 가장 큰 값(최대 빈도수)을 찾습니다.
5.  최대 빈도수와 동일한 빈도수를 가진 점수들(key)을 모두 찾아 리스트에 저장합니다.
6.  문제의 조건에 따라, 최빈수가 여러 개일 경우 가장 큰 점수를 출력해야 하므로, 위에서 찾은 점수 리스트에서 `max()` 함수를 사용하여 가장 큰 값을 출력합니다.

---

## 💻 코드
* [1204.py](1204.py)