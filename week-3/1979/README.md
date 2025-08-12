# 1979: 어디에 단어가 들어갈 수 있을까 | D2

## 문제 출처
[SWEA](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZgvQCv6GNXHBIT9&contestProbId=AV5PuPq6AaQDFAUq&probBoxId=AZh3fFV6jffHBINp&type=PROBLEM&problemBoxTitle=8%EC%9B%94+2%EC%A3%BC%EC%B0%A8%288%EC%9B%94+18%EC%9D%BC%EA%B9%8C%EC%A7%80+%ED%91%B8%EC%8B%9C%EC%98%A4%29&problemBoxCnt=8)

## 💡 접근 방식

### 1. 사용 알고리즘
* **구현(Implementation)**
* **2차원 배열 순회** 및 **상태 관리**

### 2. 문제 풀이 과정
1.  먼저 테스트 케이스의 개수 `T`를 입력받고, 각 테스트 케이스마다 퍼즐의 크기 `N`과 단어가 들어갈 칸의 길이 `K`를 입력받습니다.
2.  퍼즐의 흰색 부분(`1`)과 검은색 부분(`0`)을 나타내는 `N x N` 크기의 2차원 배열 `puzzle`을 입력받습니다.
3.  가로와 세로 방향으로 이미 길이를 계산한 칸을 표시하기 위해 `chk_h`와 `chk_v`라는 2차원 배열을 `False`로 초기화합니다.
4.  `for` 반복문을 사용하여 `puzzle`의 모든 칸 `(r, c)`를 순회합니다.
5.  `count_length_hor` 함수를 호출하여 가로 방향으로 연속된 흰색 칸의 길이를 탐색합니다.
6.  만약 해당 위치에서 시작하는 가로 길이가 `K`와 일치하면, `word_count`를 1 증가시킵니다.
7.  마찬가지로 `count_length_ver` 함수를 호출하여 세로 방향으로 길이를 탐색하고, 길이가 `K`와 일치하면 `word_count`를 1 증가시킵니다.
8.  `chk_h`와 `chk_v` 배열을 사용하여 이미 탐색한 칸은 다시 탐색하지 않도록 효율성을 높입니다.
9.  모든 칸에 대한 탐색이 끝나면, `word_count`에 저장된 최종 단어의 수를 출력 형식에 맞춰 출력합니다.

---

## 💻 코드
* [1979.py](1979.py)