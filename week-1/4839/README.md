# 4839: 이진탐색 | D2
 
## 문제 출처
[SWEA](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZgvQCv6GNXHBIT9&contestProbId=AWTLcyA6qAMDFAVT&probBoxId=AZgvQCv6GNbHBIT9&type=PROBLEM&problemBoxTitle=7%EC%9B%94&problemBoxCnt=19)

## 💡 접근 방식

### 1. 사용 알고리즘
* **이진 탐색(Binary Search)**
* **함수(Function)**를 이용한 코드 재사용

### 2. 문제 풀이 과정
1.  먼저 테스트 케이스의 개수 `T`를 입력받습니다.
2.  이진 탐색 로직은 A와 B에게 동일하게 적용되므로, **이진 탐색 과정을 함수로 정의**하여 코드의 중복을 피하고 재사용성을 높입니다.
    * `binary_search(l, r, target)` 함수는 탐색 범위의 왼쪽 끝 `l`, 오른쪽 끝 `r`, 그리고 찾고자 하는 `target` 페이지를 인자로 받습니다.
    * 탐색 횟수를 1로 초기화하고, `c = int((l+r)/2)`로 중간 페이지를 계산합니다.
    * `c`가 `target`과 같지 않은 동안 `while` 반복문을 실행합니다.
    * `c`와 `target`을 비교하여 `l` 또는 `r` 값을 갱신하고, 탐색 횟수를 1 증가시킵니다.
    * `c`가 `target`과 같아지면 반복문을 종료하고 탐색 횟수를 반환합니다.
3.  승자를 판별하는 로직 또한 함수 `who_is_winner(A, B)`로 정의합니다. 이 함수는 두 사람의 탐색 횟수를 비교하여 횟수가 더 적은 사람을 반환합니다. 횟수가 같으면 `0`을 반환합니다.
4.  각 테스트 케이스마다 책의 전체 쪽 수 `P`와 A, B가 찾을 쪽 번호 `Pa`, `Pb`를 입력받습니다.
5.  정의한 `binary_search` 함수를 각각 `Pa`와 `Pb`에 대해 호출하여 탐색 횟수 `count_a`와 `count_b`를 구합니다.
6.  `who_is_winner` 함수에 `count_a`와 `count_b`를 전달하여 결과를 얻고, 테스트 케이스 번호와 함께 출력합니다.


---

## 💻 코드
* [4839.py](4839.py)