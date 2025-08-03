# 4874: Forth | D2

## 문제 출처
[SWEA](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZgvQCv6GNXHBIT9&contestProbId=AWTQc1MKQiIDFAVT&probBoxId=AZgvQCv6GNbHBIT9&type=PROBLEM&problemBoxTitle=7%EC%9B%94&problemBoxCnt=19)

## 💡 접근 방식

### 1. 사용 알고리즘
* **스택(Stack)** 자료구조

### 2. 문제 풀이 과정
1.  먼저 테스트 케이스의 개수 `T`를 입력받습니다.
2.  각 테스트 케이스마다 공백으로 구분된 Forth 코드를 입력받아 리스트로 저장합니다.
3.  연산을 위해 숫자만 담을 `stack`을 준비합니다.
4.  Forth 코드 리스트를 순회하며 각 요소를 확인합니다.
5.  **요소가 숫자일 경우**: `try-except` 구문을 활용하여 정수로 변환하고 `stack`에 `push`합니다.
6.  **요소가 연산자(`+`, `-`, `*`, `/`)일 경우**:
    * 연산을 위해서는 스택에 최소 2개의 숫자가 있어야 하므로, `len(stack)`이 2 미만일 경우 `error`를 반환합니다.
    * 스택에서 두 개의 숫자를 `pop`하여 연산하고, 결과를 다시 스택에 `push`합니다. 이때, 후위 표기법의 특성상 먼저 `pop`한 값이 두 번째 피연산자가 됩니다.
7.  **요소가 마침표(`.`)일 경우**:
    * 연산이 모두 끝난 후에는 스택에 하나의 숫자만 남아있어야 합니다.
    * `len(stack)`이 `1`일 경우, `stack.pop()`으로 최종 결과를 가져와 출력합니다.
    * `len(stack)`이 `1`이 아니면 `error`를 반환합니다.
8.  위의 모든 과정을 처리한 후, 최종적으로 계산된 결과 또는 `error`를 테스트 케이스 번호와 함께 출력합니다.


---

## 💻 코드
* [4874.py](4874.py)