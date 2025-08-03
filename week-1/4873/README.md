# 4873: 반복문자 지우기 | D2
 
## 문제 출처
[SWEA](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZgvQCv6GNXHBIT9&contestProbId=AWTQbpTaQfEDFAVT&probBoxId=AZgvQCv6GNbHBIT9&type=PROBLEM&problemBoxTitle=7%EC%9B%94&problemBoxCnt=19)

## 💡 접근 방식

### 1. 사용 알고리즘
* **스택(Stack)** 자료구조

### 2. 문제 풀이 과정
1.  먼저 테스트 케이스의 개수 `T`를 입력받습니다.
2.  문자열에서 연속되는 문자를 지우는 작업은 스택(Stack)을 활용하여 효율적으로 처리할 수 있습니다.
3.  각 테스트 케이스마다 주어진 문자열 `s`를 순회하면서 문자를 하나씩 스택에 넣습니다.
4.  스택에 문자를 추가할 때, 스택이 비어있지 않고 현재 추가하려는 문자와 스택의 맨 위(top)에 있는 문자가 같은지 확인합니다.
5.  만약 두 문자가 같다면, 연속된 문자가 발생했으므로 스택의 맨 위 문자를 `pop`하여 지웁니다.
6.  두 문자가 다르다면, 현재 문자를 스택에 `push`(리스트의 `append`)합니다.
7.  문자열 `s`의 모든 문자에 대한 순회가 끝나면, 스택에는 반복되는 문자들이 모두 지워진 상태의 문자들만 남아있게 됩니다.
8.  최종적으로 스택에 남아있는 요소의 개수, 즉 스택의 길이를 구하여 출력 형식에 맞춰 출력합니다.


---

## 💻 코드
* [4873.py](4873.py)