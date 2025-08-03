# 4856: 색칠하기 | D2

## 문제 출처
[SWEA](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZgvQCv6GNXHBIT9&contestProbId=AWTLZMRKpsYDFAVT&probBoxId=AZgvQCv6GNbHBIT9&type=PROBLEM&problemBoxTitle=7%EC%9B%94&problemBoxCnt=19)

## 💡 접근 방식

### 1. 사용 알고리즘
* **구현(Implementation)**
* **2차원 배열(2D Array)**

### 2. 문제 풀이 과정
1.  먼저 테스트 케이스의 개수 `T`를 입력받고, 각 테스트 케이스를 순회합니다.
2.  각 테스트 케이스마다 칠할 영역의 개수 `N`을 입력받고, 10x10 크기의 2차원 리스트 `colors`를 0으로 초기화합니다. 이 리스트는 각 칸의 색상 정보를 저장하는 데 사용됩니다.
3.  `N`개의 색칠 영역 정보를 하나씩 입력받아 처리합니다. 각 정보는 왼쪽 위 좌표(`r1, c1`), 오른쪽 아래 좌표(`r2, c2`), 그리고 색상(`color`)으로 구성됩니다.
4.  각 색칠 영역에 대해, 주어진 좌표(`r1`부터 `r2`, `c1`부터 `c2`)를 순회하는 이중 반복문을 실행합니다.
5.  해당 좌표 `(r, c)`에 위치한 칸의 `colors[r][c]` 값에 현재 칠할 색상(`color`)을 더합니다.
    * 빨간색(1)으로 칠해진 칸은 값이 1이 됩니다.
    * 파란색(2)으로 칠해진 칸은 값이 2가 됩니다.
    * 빨간색과 파란색이 겹쳐 보라색이 된 칸은 `1 + 2 = 3`이 됩니다.
6.  `N`개의 모든 영역 칠하기가 끝나면, `colors` 리스트를 다시 순회하며 값이 **3**인 칸의 개수를 셉니다.
7.  이를 위해 바깥쪽 반복문으로 행을 순회하면서, 각 행(`colors[i]`)의 `count(3)` 값을 누적하여 `result` 변수에 저장합니다.
8.  최종적으로 계산된 `result`를 테스트 케이스 번호와 함께 출력 형식에 맞춰 출력합니다.


---

## 💻 코드
* [4856.py](4856.py)